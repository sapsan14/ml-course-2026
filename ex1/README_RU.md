# ex1 — EX01: Очистка данных с помощью Pandas

Русская версия. English version: [README.md](README.md)

Первое задание курса ML: загрузить «грязный» HR CSV, очистить и преобразовать его в Pandas, сохранить чистый CSV.

## Содержание

- [Файлы](#файлы)
- [Быстрый старт](#быстрый-старт)
- [Сдача (Moodle)](#сдача-moodle)

## Файлы

| Файл | Описание |
| --- | --- |
| **EX01.ipynb** | Jupyter-ноутбук с 15 шагами (шаблон курса; заполнить код). |
| **EX01_EXTRA.ipynb** | EX01-EXTRA: анализ IBM HR (EN). |
| **EX01_EXTRA_RU.ipynb** | EX01-EXTRA: анализ IBM HR (RU). |
| **dirty_dataset.csv** | Входные данные (разделитель `;`). Не открывать в Excel. |
| **ASSIGNMENT_EX01.md** | Полное описание задания, шаги и подсказки (EN). |
| **ASSIGNMENT_EX01_RU.md** | Полное описание задания, шаги и подсказки (RU). |
| **ASSIGNMENT_EX01_EXTRA.md** | Дополнительное задание EX01-EXTRA (EN). |
| **ASSIGNMENT_EX01_EXTRA_RU.md** | Дополнительное задание EX01-EXTRA (RU). |

## Быстрый старт

1. Открой `EX01.ipynb` в Cursor (расширение Jupyter) или в Google Colab.
2. Укажи путь к данным:
   - **Colab:** смонтировать Drive, положить `dirty_dataset.csv` в папку (например `MyDrive/google_colab/`), задать `path = '/content/drive/MyDrive/google_colab/dirty_dataset.csv'`.
   - **Локально:** положить `dirty_dataset.csv` рядом с ноутбуком и использовать `path = 'dirty_dataset.csv'` (в ноутбуке уже есть ветка `else`).
3. Выполни шаги 3–15 по ноутбуку и **ASSIGNMENT_EX01_RU.md**. Используй точные имена переменных: `df_col_rename`, `df_name`, `df_age`, `df_date`, `df_salary`, `df_dropped`, `df_title`, `df_dupl`, `df_dt`, `df_cat`, `df_merged`, `df_sort`, `df_col_sorted`.
4. Для сдачи: полностью запусти ноутбук в **Google Colab**, открой доступ “Anyone with the link — Viewer”, отправь ссылку в Moodle.

## Локальный запуск (проверено)

- **Зависимости:** `pandas`, `numpy`, `jupyter`, `pytz`
- **Команда (из корня репозитория):**
  ```bash
  /home/anton/projects/ml-course-2026/.venv/bin/jupyter nbconvert --execute --to notebook --inplace /home/anton/projects/ml-course-2026/ex1/EX01.ipynb
  ```
- **Русский ноутбук:**
  ```bash
  /home/anton/projects/ml-course-2026/.venv/bin/jupyter nbconvert --execute --to notebook --inplace /home/anton/projects/ml-course-2026/ex1/EX01_RU.ipynb
  ```
- **Примечание:** Команда выполняет все ячейки локально и обновляет выводы в ноутбуке.

## Примечания для автопроверки (EX01)

- Возраст: числовое преобразование, удаление невалидных строк (<0 или >120), затем медианная иммутация.
- Зарплата: иммутация пропусков средним (после фильтра по возрасту).
- Даты: `df_date` — datetime; для `df_merged` даты приводятся к строке; перед сортировкой конвертируются обратно в datetime.

## Датасет для EX01-EXTRA

- Скачайте CSV с Kaggle (IBM HR Analytics Employee Attrition & Performance).
- Альтернативная ссылка (Google Drive): https://drive.google.com/file/d/1x_cDdyA_pU71CGviivMs-7SUg-IPh_0I/view?usp=drivesdk
- Положите файл рядом с ноутбуком или в `ex1/data/`.
- Если файл в другом месте, задайте `path_override` в `EX01_EXTRA.ipynb` / `EX01_EXTRA_RU.ipynb`.

## Сдача (Moodle)

- **EX01:** ссылка на Jupyter Notebook → вставить Colab‑ссылку (EX01.ipynb).
- **EX01-EXTRA** (по желанию): отдельный ноутбук по IBM HR Analytics; отправить ссылку в соответствующее поле.

См. корневой **WORKFLOW_RU.md** для шагов Cursor vs Colab и настройки Colab.
