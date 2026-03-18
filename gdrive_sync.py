#!/usr/bin/env python3
"""
Скрипт для автоматической синхронизации файлов с Google Drive
"""

import os
import io
import json
import pickle
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Области доступа для Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Путь к файлам конфигурации
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'
SYNC_CONFIG_FILE = 'gdrive_sync_config.json'

class GDriveSync:
    def __init__(self, project_root=None):
        """Инициализация синхронизации с Google Drive"""
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.credentials_path = self.project_root / CREDENTIALS_FILE
        self.token_path = self.project_root / TOKEN_FILE
        self.config_path = self.project_root / SYNC_CONFIG_FILE
        self.service = None
        self.config = self.load_config()
        
    def load_config(self):
        """Загрузка конфигурации синхронизации"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Конфигурация по умолчанию
            default_config = {
                "sync_folders": [
                    "ex1",
                    "ex2", 
                    "ex3",
                    "ex4__auto_mpg",
                    "ex5"
                ],
                "sync_extensions": [
                    ".ipynb",
                    ".py",
                    ".md",
                    ".txt"
                ],
                "exclude_patterns": [
                    ".venv",
                    ".git",
                    "__pycache__",
                    "*.pyc"
                ],
                "gdrive_folder_name": "ml-course-2026",
                "gdrive_folder_id": None
            }
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config):
        """Сохранение конфигурации"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def authenticate(self):
        """Аутентификация в Google Drive"""
        creds = None
        
        # Загрузка сохраненных учетных данных
        if self.token_path.exists():
            with open(self.token_path, 'rb') as token:
                creds = pickle.load(token)
        
        # Если нет валидных учетных данных, запросить авторизацию
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_path.exists():
                    raise FileNotFoundError(
                        f"Файл {CREDENTIALS_FILE} не найден!\n"
                        f"Скачайте его из Google Cloud Console:\n"
                        f"1. Перейдите на https://console.cloud.google.com/\n"
                        f"2. Создайте проект или выберите существующий\n"
                        f"3. Включите Google Drive API\n"
                        f"4. Создайте OAuth 2.0 Client ID (Desktop app)\n"
                        f"5. Скачайте credentials.json в {self.project_root}"
                    )
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Сохранение учетных данных
            with open(self.token_path, 'wb') as token:
                pickle.dump(creds, token)
        
        self.service = build('drive', 'v3', credentials=creds)
        print("✓ Аутентификация успешна")
    
    def get_or_create_folder(self, folder_name, parent_id=None):
        """Получить или создать папку на Google Drive"""
        # Поиск существующей папки
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        if parent_id:
            query += f" and '{parent_id}' in parents"
        
        results = self.service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)'
        ).execute()
        
        files = results.get('files', [])
        
        if files:
            return files[0]['id']
        
        # Создание новой папки
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
        
        folder = self.service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()
        
        print(f"✓ Создана папка: {folder_name}")
        return folder.get('id')
    
    def upload_file(self, local_path, gdrive_folder_id):
        """Загрузка файла на Google Drive"""
        file_name = local_path.name
        
        # Проверка, существует ли файл на Drive
        query = f"name='{file_name}' and '{gdrive_folder_id}' in parents and trashed=false"
        results = self.service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name, modifiedTime)'
        ).execute()
        
        files = results.get('files', [])
        
        file_metadata = {'name': file_name}
        media = MediaFileUpload(str(local_path), resumable=True)
        
        if files:
            # Обновление существующего файла
            file_id = files[0]['id']
            file = self.service.files().update(
                fileId=file_id,
                media_body=media
            ).execute()
            print(f"↑ Обновлен: {local_path.relative_to(self.project_root)}")
        else:
            # Создание нового файла
            file_metadata['parents'] = [gdrive_folder_id]
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print(f"↑ Загружен: {local_path.relative_to(self.project_root)}")
        
        return file.get('id')
    
    def should_sync_file(self, file_path):
        """Проверка, нужно ли синхронизировать файл"""
        # Проверка расширения
        if self.config['sync_extensions']:
            if file_path.suffix not in self.config['sync_extensions']:
                return False
        
        # Проверка исключений
        for pattern in self.config['exclude_patterns']:
            if pattern in str(file_path):
                return False
        
        return True
    
    def sync_folder(self, local_folder, gdrive_parent_id):
        """Синхронизация локальной папки с Google Drive"""
        folder_path = self.project_root / local_folder
        
        if not folder_path.exists():
            print(f"⚠ Папка не найдена: {local_folder}")
            return
        
        # Создание папки на Drive
        gdrive_folder_id = self.get_or_create_folder(
            folder_path.name, 
            gdrive_parent_id
        )
        
        # Синхронизация файлов
        for item in folder_path.rglob('*'):
            if item.is_file() and self.should_sync_file(item):
                # Получение относительного пути
                rel_path = item.relative_to(folder_path)
                
                # Создание подпапок если нужно
                current_parent_id = gdrive_folder_id
                if rel_path.parent != Path('.'):
                    for part in rel_path.parent.parts:
                        current_parent_id = self.get_or_create_folder(
                            part, 
                            current_parent_id
                        )
                
                # Загрузка файла
                self.upload_file(item, current_parent_id)
    
    def sync_all(self):
        """Синхронизация всех настроенных папок"""
        print(f"\n{'='*60}")
        print(f"Начало синхронизации: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        # Аутентификация
        self.authenticate()
        
        # Получение или создание корневой папки
        root_folder_id = self.config.get('gdrive_folder_id')
        if not root_folder_id:
            root_folder_id = self.get_or_create_folder(
                self.config['gdrive_folder_name']
            )
            self.config['gdrive_folder_id'] = root_folder_id
            self.save_config(self.config)
        
        # Синхронизация каждой папки
        for folder in self.config['sync_folders']:
            print(f"\n📁 Синхронизация: {folder}")
            self.sync_folder(folder, root_folder_id)
        
        print(f"\n{'='*60}")
        print(f"✓ Синхронизация завершена: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")


def main():
    """Главная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Синхронизация файлов проекта с Google Drive'
    )
    parser.add_argument(
        '--project-root',
        default=None,
        help='Путь к корню проекта (по умолчанию: текущая директория)'
    )
    parser.add_argument(
        '--setup',
        action='store_true',
        help='Настроить конфигурацию синхронизации'
    )
    
    args = parser.parse_args()
    
    sync = GDriveSync(args.project_root)
    
    if args.setup:
        print("Текущая конфигурация:")
        print(json.dumps(sync.config, indent=2, ensure_ascii=False))
        print("\nДля изменения конфигурации отредактируйте файл:")
        print(f"  {sync.config_path}")
    else:
        sync.sync_all()


if __name__ == '__main__':
    main()
