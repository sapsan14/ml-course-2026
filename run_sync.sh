#!/bin/bash
# Скрипт-обертка для запуска синхронизации из cron
cd /home/anton/projects/ml-course-2026
source .venv/bin/activate
./gdrive_sync.py >> /tmp/gdrive_sync.log 2>&1
