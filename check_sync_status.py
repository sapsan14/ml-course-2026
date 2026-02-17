#!/usr/bin/env python3
"""
Скрипт для проверки статуса синхронизации с Google Drive
"""

import json
import pickle
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_FILE = 'token.pickle'
CONFIG_FILE = 'gdrive_sync_config.json'


def check_auth():
    """Проверка статуса авторизации"""
    token_path = Path(TOKEN_FILE)
    
    if not token_path.exists():
        return False, "❌ Авторизация не выполнена. Запустите ./gdrive_sync.py для авторизации."
    
    try:
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
        
        if not creds.valid:
            if creds.expired and creds.refresh_token:
                return True, "⚠️  Токен истек, но может быть обновлен автоматически."
            else:
                return False, "❌ Токен недействителен. Требуется повторная авторизация."
        
        return True, "✓ Авторизация активна"
    except Exception as e:
        return False, f"❌ Ошибка при проверке авторизации: {e}"


def get_drive_info():
    """Получение информации о Google Drive"""
    token_path = Path(TOKEN_FILE)
    
    if not token_path.exists():
        return None
    
    try:
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
        
        if creds and creds.valid:
            service = build('drive', 'v3', credentials=creds)
            about = service.about().get(fields="user,storageQuota").execute()
            return about
        
    except Exception as e:
        print(f"⚠️  Не удалось получить информацию о Drive: {e}")
        return None


def check_config():
    """Проверка конфигурации"""
    config_path = Path(CONFIG_FILE)
    
    if not config_path.exists():
        return None, "⚠️  Конфигурация не создана. Будет создана при первом запуске."
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config, "✓ Конфигурация загружена"
    except Exception as e:
        return None, f"❌ Ошибка при чтении конфигурации: {e}"


def check_credentials():
    """Проверка наличия credentials.json"""
    creds_path = Path('credentials.json')
    
    if not creds_path.exists():
        return False, "❌ Файл credentials.json не найден"
    
    try:
        with open(creds_path, 'r') as f:
            json.load(f)
        return True, "✓ Файл credentials.json найден и валиден"
    except Exception as e:
        return False, f"❌ Файл credentials.json поврежден: {e}"


def check_sync_folders(config):
    """Проверка существования папок для синхронизации"""
    if not config:
        return []
    
    results = []
    for folder in config.get('sync_folders', []):
        folder_path = Path(folder)
        exists = folder_path.exists()
        
        if exists:
            # Подсчет файлов для синхронизации
            file_count = 0
            extensions = config.get('sync_extensions', [])
            
            for ext in extensions:
                file_count += len(list(folder_path.rglob(f'*{ext}')))
            
            results.append({
                'folder': folder,
                'exists': True,
                'files': file_count
            })
        else:
            results.append({
                'folder': folder,
                'exists': False,
                'files': 0
            })
    
    return results


def format_bytes(bytes_value):
    """Форматирование размера в читаемый вид"""
    if bytes_value is None:
        return "N/A"
    
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} PB"


def main():
    """Главная функция"""
    print("=" * 70)
    print("СТАТУС СИНХРОНИЗАЦИИ С GOOGLE DRIVE")
    print("=" * 70)
    print()
    
    # Проверка credentials.json
    print("📋 Проверка учетных данных:")
    creds_ok, creds_msg = check_credentials()
    print(f"   {creds_msg}")
    print()
    
    # Проверка авторизации
    print("🔐 Проверка авторизации:")
    auth_ok, auth_msg = check_auth()
    print(f"   {auth_msg}")
    print()
    
    # Информация о Google Drive
    if auth_ok:
        print("☁️  Информация о Google Drive:")
        drive_info = get_drive_info()
        if drive_info:
            user = drive_info.get('user', {})
            quota = drive_info.get('storageQuota', {})
            
            print(f"   Пользователь: {user.get('emailAddress', 'N/A')}")
            print(f"   Имя: {user.get('displayName', 'N/A')}")
            
            if quota:
                limit = int(quota.get('limit', 0))
                usage = int(quota.get('usage', 0))
                
                if limit > 0:
                    percent = (usage / limit) * 100
                    print(f"   Использовано: {format_bytes(usage)} из {format_bytes(limit)} ({percent:.1f}%)")
                else:
                    print(f"   Использовано: {format_bytes(usage)}")
        print()
    
    # Проверка конфигурации
    print("⚙️  Проверка конфигурации:")
    config, config_msg = check_config()
    print(f"   {config_msg}")
    
    if config:
        print(f"   Папка на Drive: {config.get('gdrive_folder_name', 'N/A')}")
        print(f"   ID папки: {config.get('gdrive_folder_id', 'Не создана')}")
        print(f"   Синхронизируемые расширения: {', '.join(config.get('sync_extensions', []))}")
    print()
    
    # Проверка локальных папок
    if config:
        print("📁 Локальные папки для синхронизации:")
        folders = check_sync_folders(config)
        
        total_files = 0
        for folder_info in folders:
            status = "✓" if folder_info['exists'] else "❌"
            folder_name = folder_info['folder']
            file_count = folder_info['files']
            total_files += file_count
            
            if folder_info['exists']:
                print(f"   {status} {folder_name}: {file_count} файлов")
            else:
                print(f"   {status} {folder_name}: папка не найдена")
        
        print()
        print(f"   Всего файлов для синхронизации: {total_files}")
    print()
    
    # Проверка логов
    print("📝 Логи синхронизации:")
    log_path = Path('/tmp/gdrive_sync.log')
    if log_path.exists():
        try:
            stat = log_path.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime)
            print(f"   ✓ Лог-файл: {log_path}")
            print(f"   Последнее обновление: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Размер: {format_bytes(stat.st_size)}")
            
            # Показать последние 5 строк
            with open(log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if lines:
                    print(f"   Последние записи:")
                    for line in lines[-5:]:
                        print(f"     {line.rstrip()}")
        except Exception as e:
            print(f"   ⚠️  Ошибка чтения лога: {e}")
    else:
        print(f"   ⚠️  Лог-файл не найден (синхронизация еще не запускалась)")
    print()
    
    # Рекомендации
    print("💡 Рекомендации:")
    if not creds_ok:
        print("   1. Скачайте credentials.json из Google Cloud Console")
        print("      https://console.cloud.google.com/apis/credentials")
    
    if not auth_ok:
        print("   2. Запустите авторизацию:")
        print("      ./gdrive_sync.py")
    
    if auth_ok and config:
        print("   ✓ Все готово к синхронизации!")
        print("   Запустите: ./gdrive_sync.py")
    
    print()
    print("=" * 70)


if __name__ == '__main__':
    main()
