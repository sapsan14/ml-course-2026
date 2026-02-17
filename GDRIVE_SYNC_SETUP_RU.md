# Настройка автоматической синхронизации с Google Drive

Этот документ описывает процесс настройки автоматической синхронизации файлов проекта с Google Drive.

## Шаг 1: Создание учетных данных Google Cloud

1. **Перейдите в Google Cloud Console**
   - Откройте https://console.cloud.google.com/

2. **Создайте новый проект или выберите существующий**
   - Нажмите на выпадающий список проектов вверху страницы
   - Нажмите "New Project" (Новый проект)
   - Введите название: `ml-course-2026-sync`
   - Нажмите "Create" (Создать)

3. **Включите Google Drive API**
   - В меню навигации выберите "APIs & Services" → "Library"
   - Найдите "Google Drive API"
   - Нажмите на него и нажмите "Enable" (Включить)

4. **Создайте OAuth 2.0 Client ID**
   - Перейдите в "APIs & Services" → "Credentials"
   - Нажмите "Create Credentials" → "OAuth client ID"
   - Если появится запрос, настройте OAuth consent screen:
     - User Type: External
     - App name: `ML Course 2026 Sync`
     - User support email: ваш email
     - Developer contact: ваш email
     - Нажмите "Save and Continue"
     - Scopes: можно пропустить
     - Test users: добавьте свой email
     - Нажмите "Save and Continue"
   - Вернитесь к созданию Client ID:
     - Application type: "Desktop app"
     - Name: `ML Course Desktop Client`
     - Нажмите "Create"

5. **Скачайте credentials.json**
   - После создания появится окно с Client ID и Client Secret
   - Нажмите "Download JSON"
   - Переименуйте скачанный файл в `credentials.json`
   - Переместите его в корень проекта: `/home/anton/projects/ml-course-2026/credentials.json`

## Шаг 2: Первый запуск и авторизация

```bash
# Активируйте виртуальное окружение
cd /home/anton/projects/ml-course-2026
source .venv/bin/activate

# Сделайте скрипт исполняемым
chmod +x gdrive_sync.py

# Запустите первую синхронизацию
./gdrive_sync.py
```

При первом запуске:
1. Откроется браузер с запросом на авторизацию
2. Войдите в свой Google аккаунт
3. Разрешите доступ к Google Drive
4. После успешной авторизации будет создан файл `token.pickle`
5. Начнется синхронизация файлов

## Шаг 3: Настройка конфигурации (опционально)

Конфигурация хранится в файле `gdrive_sync_config.json`. Вы можете отредактировать его для изменения параметров синхронизации:

```json
{
  "sync_folders": [
    "ex1",
    "ex2",
    "ex3"
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
  "gdrive_folder_id": "..."
}
```

Для просмотра текущей конфигурации:
```bash
./gdrive_sync.py --setup
```

## Шаг 4: Настройка автоматической синхронизации

### Вариант A: Использование cron (рекомендуется)

Создайте скрипт-обертку для запуска из cron:

```bash
# Создайте скрипт
cat > /home/anton/projects/ml-course-2026/run_sync.sh << 'EOF'
#!/bin/bash
cd /home/anton/projects/ml-course-2026
source .venv/bin/activate
./gdrive_sync.py >> /tmp/gdrive_sync.log 2>&1
EOF

# Сделайте его исполняемым
chmod +x /home/anton/projects/ml-course-2026/run_sync.sh

# Откройте crontab для редактирования
crontab -e
```

Добавьте одну из следующих строк в crontab:

```bash
# Синхронизация каждый час
0 * * * * /home/anton/projects/ml-course-2026/run_sync.sh

# Синхронизация каждые 30 минут
*/30 * * * * /home/anton/projects/ml-course-2026/run_sync.sh

# Синхронизация каждые 15 минут
*/15 * * * * /home/anton/projects/ml-course-2026/run_sync.sh

# Синхронизация каждые 5 минут (для активной работы)
*/5 * * * * /home/anton/projects/ml-course-2026/run_sync.sh
```

### Вариант B: Использование systemd timer

Создайте systemd service и timer:

```bash
# Создайте service файл
mkdir -p ~/.config/systemd/user/
cat > ~/.config/systemd/user/gdrive-sync.service << 'EOF'
[Unit]
Description=Google Drive Sync for ML Course
After=network.target

[Service]
Type=oneshot
WorkingDirectory=/home/anton/projects/ml-course-2026
ExecStart=/home/anton/projects/ml-course-2026/.venv/bin/python /home/anton/projects/ml-course-2026/gdrive_sync.py
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
EOF

# Создайте timer файл
cat > ~/.config/systemd/user/gdrive-sync.timer << 'EOF'
[Unit]
Description=Google Drive Sync Timer
Requires=gdrive-sync.service

[Timer]
OnBootSec=5min
OnUnitActiveSec=15min

[Install]
WantedBy=timers.target
EOF

# Перезагрузите systemd и включите timer
systemctl --user daemon-reload
systemctl --user enable gdrive-sync.timer
systemctl --user start gdrive-sync.timer

# Проверьте статус
systemctl --user status gdrive-sync.timer
systemctl --user list-timers
```

## Шаг 5: Ручная синхронизация

Для ручного запуска синхронизации в любое время:

```bash
cd /home/anton/projects/ml-course-2026
source .venv/bin/activate
./gdrive_sync.py
```

## Просмотр логов

### Для cron:
```bash
tail -f /tmp/gdrive_sync.log
```

### Для systemd:
```bash
journalctl --user -u gdrive-sync.service -f
```

## Проверка синхронизации

После запуска синхронизации:
1. Откройте https://drive.google.com/
2. Найдите папку `ml-course-2026`
3. Проверьте, что файлы из папок `ex1`, `ex2`, `ex3` загружены

## Устранение неполадок

### Ошибка: "credentials.json не найден"
- Убедитесь, что файл `credentials.json` находится в корне проекта
- Проверьте путь: `/home/anton/projects/ml-course-2026/credentials.json`

### Ошибка авторизации
- Удалите файл `token.pickle`
- Запустите синхронизацию снова для повторной авторизации

### Файлы не синхронизируются
- Проверьте конфигурацию в `gdrive_sync_config.json`
- Убедитесь, что расширения файлов указаны в `sync_extensions`
- Проверьте, что файлы не попадают под `exclude_patterns`

## Безопасность

⚠️ **Важно:**
- Файлы `credentials.json` и `token.pickle` содержат конфиденциальную информацию
- Убедитесь, что они добавлены в `.gitignore`
- Не публикуйте эти файлы в публичных репозиториях

## Дополнительные возможности

### Добавление новых папок для синхронизации

Отредактируйте `gdrive_sync_config.json`:
```json
{
  "sync_folders": [
    "ex1",
    "ex2",
    "ex3",
    "ex4",
    "notes"
  ]
}
```

### Изменение расширений файлов

```json
{
  "sync_extensions": [
    ".ipynb",
    ".py",
    ".md",
    ".txt",
    ".csv",
    ".json"
  ]
}
```
