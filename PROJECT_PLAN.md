# Project plan — ML course 2026

Russian version: [PROJECT_PLAN_RU.md](PROJECT_PLAN_RU.md)

## English

### Goals

1. Complete TalTech ML course assignments (Pandas, Colab, later ML topics).
2. Keep all code and data in one repo (`ml-course-2026`) with clear structure.
3. Prefer developing in Cursor; use Colab only where required (e.g. EX01 submission).

### Phases

| Phase | Content | Outcome |
| --- | --- | --- |
| **1. Setup** | Repo, ex1 folder, README, WORKFLOW, assignment docs | Can open project in Cursor and follow steps |
| **2. EX01** | Solve EX01 (Pandas cleaning) in notebook; test locally; run in Colab; submit link in Moodle | EX01 passed, clean CSV saved |
| **3. EX01-EXTRA** (optional) | IBM HR Analytics on Kaggle: load, explore, groupby, simple analysis (see `ex1/ASSIGNMENT_EX01_EXTRA.md`) | Optional notebook submitted |
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
