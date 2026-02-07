# Настройка репозитория GitHub

Русская версия. English version: [GITHUB_SETUP.md](GITHUB_SETUP.md)

Проект готов локально. Чтобы выложить его на GitHub:

## Содержание

- [1. Создать репозиторий на GitHub](#1-создать-репозиторий-на-github)
- [2. Отправить с локальной машины](#2-отправить-с-локальной-машины)
- [3. Опционально: добавить правило Cursor для этого репозитория](#3-опционально-добавить-правило-cursor-для-этого-репозитория)

## 1. Создать репозиторий на GitHub

1. Откройте [github.com/new](https://github.com/new).
2. **Название репозитория:** `ml-course-2026`
3. **Описание:** `TalTech Machine Learning for Engineers 2026 — assignments, notebooks, pandas/Colab`
4. Выберите **Public** (или Private, если хотите).
5. **Не добавляйте** README, .gitignore или лицензию (они уже есть).
6. Нажмите **Create repository**.

## 2. Отправить с локальной машины

В терминале, из папки проекта:

```bash
cd /home/anton/projects/ml-course-2026
git init
git add .
git commit -m "Initial: EX01 assignment, README, workflow, project plan"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ml-course-2026.git
git push -u origin main
```

Замените `YOUR_USERNAME` на ваш GitHub‑логин.

Если используете SSH:

```bash
git remote add origin git@github.com:YOUR_USERNAME/ml-course-2026.git
git push -u origin main
```

## 3. Опционально: добавить правило Cursor для этого репозитория

Чтобы ИИ понимал контекст курса и EX01, можно добавить правило:

- Создать `.cursor/rules/ml-course.mdc` с короткой заметкой о том, что это репозиторий TalTech ML 2026, EX01 — очистка в Pandas, имена переменных должны совпадать с заданием, и использовать ASSIGNMENT_EX01.md для шагов и подсказок.

После этого можно клонировать или открывать репозиторий из GitHub в Cursor на любом компьютере.
