# Project plan — ML course 2026

## English

### Goals

1. Complete TalTech ML course assignments (Pandas, Colab, later ML topics).
2. Keep all code and data in one repo (`ml-course-2026`) with clear structure.
3. Prefer developing in Cursor; use Colab only where required (e.g. EX01 submission).

### Phases

| Phase | Content | Outcome |
|-------|---------|--------|
| **1. Setup** | Repo, ex1 folder, README, WORKFLOW, assignment docs | Can open project in Cursor and follow steps |
| **2. EX01** | Solve EX01 (Pandas cleaning) in notebook; test locally; run in Colab; submit link in Moodle | EX01 passed, clean CSV saved |
| **3. EX01-EXTRA** (optional) | IBM HR Analytics on Kaggle: load, explore, groupby, simple analysis | Optional notebook submitted |
| **4. Later** | ex2, ex3, … as course progresses | Repo grows with each assignment |

### EX01 scope (detailed)

- **Input:** `dirty_dataset.csv` (HR-style CSV; semicolon-separated).
- **Steps (1–15):** load from Drive/path → overview → rename columns → split name → clean age (impute, filter invalid, int) → clean dates (datetime) → clean salary (impute, int) → drop Parkimine → clean Amet (FI, OP, HR, IT) → drop duplicates (Eesnimi, Perekonnanimi) → add Aastat_liitumisest, Palk_kategooria → merge building table → sort by Liitumise_kuupäev (desc) → reorder columns → save CSV.
- **Output:** Clean DataFrame with columns Id, Liitumise_kuupäev, Aastat_liitumisest, Amet, Eesnimi, Perekonnanimi, Palk, Palk_kategooria, Vanus; saved as CSV (e.g. in Drive).
- **Submission:** Google Colab notebook link (EX01.ipynb), shared as “Anyone with the link — Viewer”.

### Success criteria

- Notebook runs from top to bottom in Colab without errors.
- Variable names match what the autotester expects (e.g. `df_col_rename`, `df_name`, `df_age`, …).
- Final CSV and DataFrame structure match assignment description and reference images.

---

## Русский

### Цели

1. Выполнять задания курса TalTech по машинному обучению (Pandas, Colab, далее темы ML).
2. Хранить весь код и данные в одном репозитории `ml-course-2026` с понятной структурой.
3. Разрабатывать по возможности в Cursor; Colab использовать только там, где это требуется (например, сдача EX01).

### Этапы

| Этап | Содержание | Результат |
|------|------------|------------|
| **1. Настройка** | Репо, папка ex1, README, WORKFLOW, описание заданий | Можно открыть проект в Cursor и следовать шагам |
| **2. EX01** | Решить EX01 (очистка в Pandas) в ноутбуке; проверить локально; запустить в Colab; сдать ссылку в Moodle | EX01 зачтён, чистый CSV сохранён |
| **3. EX01-EXTRA** (по желанию) | IBM HR Analytics с Kaggle: загрузка, разведка, groupby, простой анализ | По желанию сданный ноутбук |
| **4. Дальше** | ex2, ex3, … по мере курса | Репо обрастает заданиями |

### Объём EX01 (кратко)

- **Вход:** `dirty_dataset.csv` (CSV в стиле HR; разделитель `;`).
- **Шаги (1–15):** загрузка с Drive/пути → обзор → переименование столбцов → разбиение имени → очистка возраста (имputation, отбор допустимых, int) → очистка дат (datetime) → очистка зарплаты (imputation, int) → удаление столбца Parkimine → приведение Amet (FI, OP, HR, IT) → удаление дубликатов по (Eesnimi, Perekonnanimi) → добавление Aastat_liitumisest и Palk_kategooria → слияние с таблицей зданий → сортировка по Liitumise_kuupäev (убыв.) → переупорядочивание столбцов → сохранение CSV.
- **Выход:** «Чистый» DataFrame с столбцами Id, Liitumise_kuupäev, Aastat_liitumisest, Amet, Eesnimi, Perekonnanimi, Palk, Palk_kategooria, Vanus; сохранение в CSV (например, в Drive).
- **Сдача:** ссылка на ноутбук в Google Colab (EX01.ipynb), доступ «Anyone with the link — Viewer».

### Критерии успеха

- Ноутбук выполняется в Colab от начала до конца без ошибок.
- Имена переменных совпадают с ожиданиями автотеста (`df_col_rename`, `df_name`, `df_age`, …).
- Итоговый CSV и структура DataFrame соответствуют описанию задания и эталонным картинкам.
