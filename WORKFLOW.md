# Workflow: Cursor + Google Colab (step-by-step)

## English

### Do you need both Cursor and Colab?

- **Cursor:** Use for editing the notebook, running cells locally (if you have Jupyter), and getting AI help. You can do most of the work here.
- **Colab:** **Required for EX01 submission.** Moodle expects a **link to a Google Colab notebook**. So you must open your notebook in Colab, run it there at least once, and submit the Colab link.

**Recommended:** Develop in Cursor → when ready, upload to Drive and open in Colab → Run all → share link → submit in Moodle.

---

### Option A: Google Colab extension inside Cursor/VS Code

You can **run Colab’s runtime directly inside Cursor** using the official **Google Colab** extension (no need to switch to the browser for running code).

- **Install:** In Cursor press `Ctrl+Shift+X` → search **“Google Colab”** → Install the extension by **Google** ([Marketplace](https://marketplace.visualstudio.com/items?itemName=Google.colab)).
- **Use:** Open `ex1/EX01.ipynb` → click **“Select Kernel”** (top right) → choose **Colab** → sign in with Google when asked. Cells then run on Colab’s cloud (same backend as colab.research.google.com).
- **Benefits:** Colab’s free GPU/TPU and environment, plus Cursor’s editor, Git, and AI in one place. No need to upload the notebook to Drive just to run it.
- **For Moodle submission:** You still need a **shareable Colab link**. Either: (1) upload the same notebook to Google Drive and open it once in the browser at [colab.research.google.com](https://colab.research.google.com) → Share → copy link, or (2) use the extension’s “Manage sessions” (Colab → Connect dropdown) to get a web link if available.

Reference: [Run Google Colab inside VS Code (Medium)](https://medium.com/google-developer-experts/run-google-colab-inside-vs-code-complete-step-by-step-tutorial-8ce4a1e804c0). The article mentions installing from a `.vsix` file; the same extension is available from the Extensions panel by searching “Google Colab”.

---

### Step 1: Open the project in Cursor

1. Open folder: `File → Open Folder` → choose `ml-course-2026`.
2. You’ll see `ex1/EX01.ipynb`, `ex1/dirty_dataset.csv`, and the docs.

---

### Step 2: Jupyter in Cursor (run notebook locally)

1. Install **Jupyter** extension in Cursor if you don’t have it:  
   `Ctrl+Shift+X` (Extensions) → search “Jupyter” → install **Jupyter** (Microsoft).
2. Select a **Python interpreter**: `Ctrl+Shift+P` → “Python: Select Interpreter” → pick one with pandas (or create a venv and install `pandas numpy jupyter pytz`).
3. Open `ex1/EX01.ipynb`. Cursor/VS Code will show it as a notebook with cells.
4. In the notebook, the code already uses `path = 'dirty_dataset.csv'` when not in Colab, so with `dirty_dataset.csv` in the same folder (`ex1/`) it will load correctly.
5. Run cells with the “Run” button next to each cell or with `Shift+Enter`.

**Alternative:** Use the **Google Colab** extension (see “Option A” above) to run the notebook with Colab’s kernel inside Cursor — no browser needed for execution.

---

### Step 3: Google Colab setup (for submission)

1. Go to [Google Drive](https://drive.google.com).
2. Create a folder, e.g. **google_colab**.
3. Upload into that folder:
   - `ex1/EX01.ipynb`
   - `ex1/dirty_dataset.csv`
4. **Do not** open `dirty_dataset.csv` in Excel before uploading (Excel can change the format).
5. In Drive, double‑click **EX01.ipynb** → it opens in **Google Colab** (or right‑click → Open with → Google Colaboratory).
6. In Colab: **File → Save a copy in Drive** so you have your own editable copy.
7. Mount Drive: in the first code cell that has `drive.mount(...)`, run it and allow access when asked.
8. Make sure `path` points to your CSV, e.g.  
   `path = '/content/drive/MyDrive/google_colab/dirty_dataset.csv'`.

---

### Step 4: Solve the assignment

1. Work through steps 3–15 in the notebook (see **ex1/ASSIGNMENT_EX01.md** for details and LLM prompts).
2. Use the **exact variable names**: `df_col_rename`, `df_name`, `df_age`, `df_date`, `df_salary`, `df_dropped`, `df_title`, `df_dupl`, `df_dt`, `df_cat`, `df_merged`, `df_sort`, `df_col_sorted`.
3. You can write and test code in Cursor, then copy the notebook (or only the changed cells) to Drive and run again in Colab to confirm.

---

### Step 5: Submit in Moodle

1. In **Colab**, run **Runtime → Run all** and check that everything runs without errors.
2. **Share the notebook:** click **Share** (top right) → set “General access” to **Anyone with the link** → Link access to **Viewer** → Copy link.
3. In **Moodle**, open the EX01 assignment (Jupyter Notebook URL) and paste this Colab link.
4. Submit.

---

### Optional: EX01-EXTRA (IBM HR Analytics)

- Dataset: [Kaggle — IBM HR Analytics Employee Attrition](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).
- Create a **separate** notebook (e.g. EX01-EXTRA.ipynb), do the required exploration and analysis, then upload to Colab/Drive and submit its link in the EX01-EXTRA submission box on Moodle.

---

## Русский: Пошаговый workflow

### Нужны ли и Cursor, и Colab?

- **Cursor:** для правок ноутбука, запуска ячеек локально (если есть Jupyter) и помощи ИИ. Большую часть работы можно делать здесь.
- **Colab:** **нужен для сдачи EX01.** В Moodle сдаётся **ссылка на ноутбук в Google Colab**. Значит, нужно открыть ноутбук в Colab, хотя бы раз полностью запустить и отправить ссылку.

**Вариант: расширение Google Colab в Cursor.** Можно запускать ноутбук **внутри Cursor** на рантайме Colab: установить расширение **Google Colab** (`Ctrl+Shift+X` → поиск «Google Colab» → установить от Google), открыть `ex1/EX01.ipynb` → Select Kernel → **Colab** → войти в Google. Ячейки будут выполняться в облаке Colab. Для сдачи в Moodle всё равно понадобится ссылка на ноутбук в браузере (загрузить .ipynb в Drive и открыть в colab.research.google.com → Share). Подробнее: [Run Google Colab inside VS Code (Medium)](https://medium.com/google-developer-experts/run-google-colab-inside-vs-code-complete-step-by-step-tutorial-8ce4a1e804c0).

**Рекомендация:** разрабатывать в Cursor → когда готово — загрузить в Drive и открыть в Colab → Run all → скопировать ссылку → сдать в Moodle.

---

### Шаг 1: Открыть проект в Cursor

1. `File → Open Folder` → папка `ml-course-2026`.
2. Внутри: `ex1/EX01.ipynb`, `ex1/dirty_dataset.csv` и документация.

---

### Шаг 2: Jupyter в Cursor (локальный запуск)

1. Установить расширение **Jupyter**: `Ctrl+Shift+X` → поиск “Jupyter” → установить **Jupyter** (Microsoft).
2. Выбрать интерпретатор Python: `Ctrl+Shift+P` → “Python: Select Interpreter” (нужен интерпретатор с pandas или venv с `pandas numpy jupyter pytz`).
3. Открыть `ex1/EX01.ipynb`. Cursor отобразит ячейки.
4. В ноутбуке при локальном запуске уже стоит `path = 'dirty_dataset.csv'`, так что при наличии `dirty_dataset.csv` в `ex1/` данные подгрузятся.
5. Запуск ячеек: кнопка Run у ячейки или `Shift+Enter`.

Отдельного “плагина Colab” для Cursor нет. Colab — это сайт; ноутбук открываете в браузере. В Cursor вы только редактируете и при желании запускаете локально.

---

### Шаг 3: Настройка Google Colab (для сдачи)

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

### Шаг 4: Решение задания

1. Выполнить шаги 3–15 в ноутбуке (подробно и подсказки для ИИ — в **ex1/ASSIGNMENT_EX01.md**).
2. Использовать **точные имена переменных**: `df_col_rename`, `df_name`, `df_age`, `df_date`, `df_salary`, `df_dropped`, `df_title`, `df_dupl`, `df_dt`, `df_cat`, `df_merged`, `df_sort`, `df_col_sorted`.
3. Можно писать и проверять код в Cursor, затем обновить ноутбук в Drive и перезапустить в Colab.

---

### Шаг 5: Сдача в Moodle

1. В **Colab**: **Runtime → Run all**, убедиться, что всё выполняется без ошибок.
2. **Поделиться:** кнопка **Share** (справа сверху) → “General access” → **Anyone with the link** → доступ по ссылке: **Viewer** → скопировать ссылку.
3. В **Moodle** открыть задание EX01 (поле “Jupyter Notebook URL”), вставить ссылку на Colab и отправить.

---

### По желанию: EX01-EXTRA

- Датасет: [Kaggle — IBM HR Analytics Employee Attrition](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).
- Сделать **отдельный** ноутбук (например EX01-EXTRA.ipynb), выполнить требуемый анализ, загрузить в Colab/Drive и сдать ссылку в форме EX01-EXTRA в Moodle.
