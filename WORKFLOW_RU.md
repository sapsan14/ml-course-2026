# Workflow: Cursor + Google Colab (пошагово)

Русская версия. English version: [WORKFLOW.md](WORKFLOW.md)

## Содержание

- [Нужно ли использовать и Cursor, и Colab?](#нужно-ли-использовать-и-cursor-и-colab)
- [Вариант A: расширение Google Colab внутри Cursor/VS Code](#вариант-a-расширение-google-colab-внутри-cursorvs-code)
- [Шаг 1: Открыть проект в Cursor](#шаг-1-открыть-проект-в-cursor)
- [Шаг 2: Jupyter в Cursor (локальный запуск)](#шаг-2-jupyter-в-cursor-локальный-запуск)
- [Шаг 3: Настройка Google Colab (для сдачи)](#шаг-3-настройка-google-colab-для-сдачи)
- [Шаг 4: Решение задания](#шаг-4-решение-задания)
- [Шаг 5: Сдача в Moodle](#шаг-5-сдача-в-moodle)
- [По желанию: EX01-EXTRA](#по-желанию-ex01-extra)

## Нужно ли использовать и Cursor, и Colab?

- **Cursor:** для правок ноутбука, запуска ячеек локально (если есть Jupyter) и помощи ИИ. Большую часть работы можно делать здесь.
- **Colab:** **обязателен для сдачи EX01.** В Moodle сдаётся **ссылка на ноутбук в Google Colab**. Значит, нужно открыть ноутбук в Colab, хотя бы раз полностью запустить и отправить ссылку.

**Рекомендация:** разрабатывать в Cursor → когда готово — загрузить в Drive и открыть в Colab → Run all → скопировать ссылку → сдать в Moodle.

---

## Вариант A: расширение Google Colab внутри Cursor/VS Code

Можно запускать Colab-рантайм **внутри Cursor** с помощью официального расширения **Google Colab** (без переключения в браузер).

- **Установка:** `Ctrl+Shift+X` → поиск “Google Colab” → установить расширение от **Google** ([Marketplace](https://marketplace.visualstudio.com/items?itemName=Google.colab)).
- **Использование:** открыть `ex1/EX01.ipynb` → **Select Kernel** (справа сверху) → выбрать **Colab** → войти в Google. Ячейки будут выполняться на облачном рантайме Colab.
- **Плюсы:** облачная среда Colab + редактор Cursor в одном месте.
- **Для сдачи:** всё равно нужна **ссылка на Colab-ноутбук**. Либо загрузите .ipynb в Drive и откройте в браузере (colab.research.google.com → Share), либо попробуйте получить ссылку через “Manage sessions”, если доступно.

Справка: [Run Google Colab inside VS Code (Medium)](https://medium.com/google-developer-experts/run-google-colab-inside-vs-code-complete-step-by-step-tutorial-8ce4a1e804c0).

---

## Шаг 1: Открыть проект в Cursor

1. `File → Open Folder` → папка `ml-course-2026`.
2. Внутри: `ex1/EX01.ipynb`, `ex1/dirty_dataset.csv` и документация.

---

## Шаг 2: Jupyter в Cursor (локальный запуск)

1. Установить расширение **Jupyter**: `Ctrl+Shift+X` → поиск “Jupyter” → установить **Jupyter** (Microsoft).
2. Выбрать интерпретатор Python: `Ctrl+Shift+P` → “Python: Select Interpreter” (нужен интерпретатор с pandas или venv с `pandas numpy jupyter pytz`).
3. Открыть `ex1/EX01.ipynb`. Cursor отобразит ячейки.
4. При локальном запуске уже стоит `path = 'dirty_dataset.csv'`, так что при наличии файла в `ex1/` данные подгрузятся.
5. Запуск ячеек: кнопка Run у ячейки или `Shift+Enter`.

---

## Шаг 3: Настройка Google Colab (для сдачи)

1. Зайти на [Google Drive](https://drive.google.com).
2. Создать папку, например **google_colab**.
3. Загрузить в неё:
   - `ex1/EX01.ipynb`
   - `ex1/dirty_dataset.csv`
4. **Не открывать** `dirty_dataset.csv` в Excel перед загрузкой (Excel может изменить формат).
5. В Drive дважды кликнуть по **EX01.ipynb** → откроется в **Google Colab** (или ПКМ → Открыть с помощью → Google Colaboratory).
6. В Colab: **File → Save a copy in Drive**, чтобы была своя копия для правок.
7. Смонтировать Drive: выполнить ячейку с `drive.mount(...)`, выдать доступ по запросу.
8. Убедиться, что `path` указывает на CSV, например:  
   `path = '/content/drive/MyDrive/google_colab/dirty_dataset.csv'`.

---

## Шаг 4: Решение задания

1. Выполнить шаги 3–15 в ноутбуке (подробно и подсказки для ИИ — в **ex1/ASSIGNMENT_EX01_RU.md**).
2. Использовать **точные имена переменных**: `df_col_rename`, `df_name`, `df_age`, `df_date`, `df_salary`, `df_dropped`, `df_title`, `df_dupl`, `df_dt`, `df_cat`, `df_merged`, `df_sort`, `df_col_sorted`.
3. Можно писать и проверять код в Cursor, затем обновить ноутбук в Drive и перезапустить в Colab.

---

## Шаг 5: Сдача в Moodle

1. В **Colab**: **Runtime → Run all**, убедиться, что всё выполняется без ошибок.
2. **Поделиться:** кнопка **Share** (справа сверху) → “General access” → **Anyone with the link** → доступ по ссылке: **Viewer** → скопировать ссылку.
3. В **Moodle** открыть задание EX01 (поле “Jupyter Notebook URL”), вставить ссылку на Colab и отправить.

---

## По желанию: EX01-EXTRA

- Датасет: [Kaggle — IBM HR Analytics Employee Attrition](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).
- Сделать **отдельный** ноутбук (например EX01-EXTRA.ipynb), выполнить требования **ex1/ASSIGNMENT_EX01_EXTRA_RU.md**, загрузить в Colab/Drive и сдать ссылку в форме EX01-EXTRA в Moodle.
