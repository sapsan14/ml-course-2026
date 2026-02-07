# ex1 — EX01: Data cleaning with Pandas

First assignment of the ML course: load a dirty HR CSV, clean and transform it with Pandas, save a clean CSV.

Russian version: [README_RU.md](README_RU.md)

## Files

| File | Description |
| --- | --- |
| **EX01.ipynb** | Jupyter notebook with 15 steps (template from course; fill in the code). |
| **EX01_EXTRA.ipynb** | Optional EX01-EXTRA analysis notebook (IBM HR dataset). |
| **EX01_EXTRA_RU.ipynb** | Russian version of EX01-EXTRA analysis notebook. |
| **dirty_dataset.csv** | Input data (semicolon-separated). Do not open in Excel. |
| **ASSIGNMENT_EX01.md** | Full task description, steps, and LLM prompts (EN). |
| **ASSIGNMENT_EX01_RU.md** | Full task description, steps, and prompts (RU). |
| **ASSIGNMENT_EX01_EXTRA.md** | Optional EX01-EXTRA assignment (EN). |
| **ASSIGNMENT_EX01_EXTRA_RU.md** | Optional EX01-EXTRA assignment (RU). |

## Quick start

1. Open `EX01.ipynb` in Cursor (Jupyter extension) or in Google Colab.
2. Set the data path:
   - **Colab:** Mount Drive, put `dirty_dataset.csv` in a folder (e.g. `MyDrive/google_colab/`), set `path = '/content/drive/MyDrive/google_colab/dirty_dataset.csv'`.
   - **Local:** Put `dirty_dataset.csv` in the same folder as the notebook and use `path = 'dirty_dataset.csv'` (the notebook already has an `else` branch for this).
3. Solve steps 3–15 following the notebook and **ASSIGNMENT_EX01.md**. Use the exact variable names: `df_col_rename`, `df_name`, `df_age`, `df_date`, `df_salary`, `df_dropped`, `df_title`, `df_dupl`, `df_dt`, `df_cat`, `df_merged`, `df_sort`, `df_col_sorted`.
4. For submission: run the full notebook in **Google Colab**, share with “Anyone with the link — Viewer”, submit that link in Moodle.

## Local run (verified)

- **Dependencies:** `pandas`, `numpy`, `jupyter`, `pytz`
- **Command (from repo root):**
  ```bash
  /home/anton/projects/ml-course-2026/.venv/bin/jupyter nbconvert --execute --to notebook --inplace /home/anton/projects/ml-course-2026/ex1/EX01.ipynb
  ```
- **Russian notebook:**
  ```bash
  /home/anton/projects/ml-course-2026/.venv/bin/jupyter nbconvert --execute --to notebook --inplace /home/anton/projects/ml-course-2026/ex1/EX01_RU.ipynb
  ```
- **Notes:** This runs all cells locally and updates outputs inside the notebook.

## Autograder notes (EX01)

- Age: convert to numeric, drop invalid rows (<0 or >120), then impute missing with median.
- Salary: impute missing with mean (computed after age filtering).
- Dates: keep `df_date` as datetime; `df_merged` uses string dates for merge; convert back to datetime before sorting and final outputs.

## EX01-EXTRA dataset

- Download the CSV from Kaggle (IBM HR Analytics Employee Attrition & Performance).
- Place the file next to the notebook or into `ex1/data/`.
- If you store it elsewhere, set `path_override` in `EX01_EXTRA.ipynb` / `EX01_EXTRA_RU.ipynb`.

## Submission (Moodle)

- **EX01:** Jupyter Notebook URL → paste your Colab link (EX01.ipynb).
- **EX01-EXTRA** (optional): separate notebook for IBM HR Analytics; submit link in its submission box.

See project root **WORKFLOW.md** for Cursor vs Colab workflow and Colab setup (RU: **WORKFLOW_RU.md**).
