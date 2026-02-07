# EX01 — Data cleaning and processing with Pandas

**Course:** TalTech ML for Engineers 2026  
**Moodle:** EX01 - Notebook Link (section id 146327)  
**Data:** `dirty_dataset.csv` (do not open in Excel before use — it can change formatting).

Russian version: [ASSIGNMENT_EX01_RU.md](ASSIGNMENT_EX01_RU.md)

---

## English: Task overview and steps

### Objective

Clean and structure a CSV used by HR: load it, fix column names and values, create new columns, sort and reorder, save as a new CSV. Use **Pandas**; follow the notebook steps 1–15 and use the **exact variable names** required by the autotester.

### Data

- **File:** `dirty_dataset.csv`
- **Separator:** `;`
- **Columns (raw):** Id, Nimi1, Vanus, Liitumise_Kuupäev, Tööala, Palk, Parkimine
- **Issues:** mixed formats, missing values, duplicates, invalid ages/salaries, department names to normalize (Finance→FI, Ops→OP, HR, IT), date formats.

### Steps 1–15 (summary)

1. **Load data** — Mount Drive (in Colab) or use local path. Set `path` to CSV location. Read with `pd.read_csv(path, sep=";")` into `df`.
2. **Overview** — Use `df.info()`, `df.head()`, `df.tail()`, `df.describe()`, check duplicates and missing values.
3. **Column names** — Copy to `df_col_rename`. Rename: `Tööala` → `Amet`, `Liitumise_Kuupäev` → `Liitumise_kuupäev`. Keep other names consistent.
4. **Names** — Copy to `df_name`. Split full name into `Eesnimi` and `Perekonnanimi` (first/last); handle extra spaces.
5. **Age** — Copy to `df_age`. Impute missing; filter invalid (e.g. negative or > 120); ensure integer type.
6. **Dates** — Copy to `df_date`. Normalize date strings to one format, convert to `pd.to_datetime()`.
7. **Salary** — Copy to `df_salary`. Impute missing; ensure integer; handle invalid values.
8. **Drop Parkimine** — Copy to `df_dropped`. Remove column `Parkimine`.
9. **Department (Amet)** — Copy to `df_title`. Allow only FI, OP, HR, IT; map Finance→FI, Ops→OP, etc.; impute if needed.
10. **Duplicates** — Copy to `df_dupl`. Drop duplicates by (Eesnimi, Perekonnanimi), keep first.
11. **New columns** — From `df_dupl` → `df_dt`: add `Aastat_liitumisest` (full years since Liitumise_kuupäev). From `df_dt` → `df_cat`: add `Palk_kategooria`: "madal" (0–29999), "keskmine" (30000–59999), "kõrge" (60000+); else NaN.
12. **Merge building** — Reset index to get clean integer index. Create `df_hoone` with Id and Hoone (mapping given in notebook). Merge into main table → `df_merged`.
13. **Sort** — Copy to `df_sort`. Sort by Liitumise_kuupäev descending; reset index so it goes 0, 1, 2, …
14. **Column order** — Copy to `df_col_sorted`. Order: Id, Liitumise_kuupäev, Aastat_liitumisest, Amet, Eesnimi, Perekonnanimi, Palk, Palk_kategooria, Vanus.
15. **Save CSV** — Save `df_col_sorted` to CSV (e.g. Drive path), `index=False`.

### Submission

- Work in **Google Colab** for final run.
- Notebook name: **EX01.ipynb**.
- Share: **Anyone with the link** — **Viewer**.
- Submit that link in Moodle (EX01 - Notebook Link).

---

## LLM-readable prompts (for Cursor / AI assistant)

Copy-paste these when asking an AI to help with a specific step. Use the exact variable names.

- **Step 3 — Column rename**  
  "In a copy of the DataFrame named `df_col_rename`, rename column `Tööala` to `Amet` and `Liitumise_Kuupäev` to `Liitumise_kuupäev`. Keep all other column names unchanged. Use pandas."

- **Step 4 — Split name**  
  "From `df_col_rename`, create `df_name` as a copy. Add columns `Eesnimi` and `Perekonnanimi` by splitting the existing full-name column (e.g. Nimi1) on the first space, stripping extra spaces. Handle edge cases (single name, multiple spaces)."

- **Step 5 — Age**  
  "From `df_name`, create `df_age`. In column Vanus: impute missing values (e.g. with median), filter out invalid ages (e.g. not in 0–120 or non-numeric like 'thirty'), convert to integer. Keep only valid rows."

- **Step 6 — Dates**  
  "From `df_age`, create `df_date`. Column Liitumise_kuupäev: normalize different date string formats (e.g. 2023/02/20, 2023.07.20) and convert to pandas datetime with pd.to_datetime()."

- **Step 7 — Salary**  
  "From `df_date`, create `df_salary`. In Palk: impute missing (e.g. median), convert to integer, drop or fix invalid (e.g. negative)."

- **Step 8 — Drop column**  
  "From `df_salary`, create `df_dropped` and remove the column Parkimine."

- **Step 9 — Department**  
  "From `df_dropped`, create `df_title`. In Amet, allow only FI, OP, HR, IT. Map Finance→FI, Ops→OP (and similar). Impute remaining missing if needed."

- **Step 10 — Duplicates**  
  "From `df_title`, create `df_dupl`. Drop duplicate rows by (Eesnimi, Perekonnanimi), keeping the first occurrence."

- **Step 11 — New columns**  
  "From `df_dupl` create `df_dt`: add column Aastat_liitumisest = full years from Liitumise_kuupäev to today. From `df_dt` create `df_cat`: add Palk_kategooria: 'madal' if 0<=Palk<30000, 'keskmine' if 30000<=Palk<60000, 'kõrge' if Palk>=60000, else NaN. Use pandas."

- **Step 12 — Building merge**  
  "Create a small DataFrame df_hoone with columns Id and Hoone (mapping from the assignment: 124→A, 152→B, 632→C, 853→A, 963→C, 84→B, 863→A, 973→A, 111→B, 142→C). Reset index on the main table and merge df_hoone on Id. Store result in df_merged."

- **Step 13 — Sort**  
  "From df_merged create df_sort: sort by Liitumise_kuupäev descending, then reset_index(drop=True)."

- **Step 14 — Column order**  
  "From df_sort create df_col_sorted with columns in this order: Id, Liitumise_kuupäev, Aastat_liitumisest, Amet, Eesnimi, Perekonnanimi, Palk, Palk_kategooria, Vanus."

- **Step 15 — Save**  
  "Save df_col_sorted to CSV with index=False. In Colab use a path under /content/drive/MyDrive/...; locally use a path like clean_dataset_TIMESTAMP.csv."

---

## Reference image URLs (from notebook)

- Step 3: [03_veergude_nimetamine.png](https://cs.taltech.ee/services/forge/maksim.tsopov/itx0020-images/raw/branch/main/ex01_pandas/03_veergude_nimetamine.png)  
- Step 4: [04_nimede_lahutamine.png](https://cs.taltech.ee/services/forge/maksim.tsopov/itx0020-images/raw/branch/main/ex01_pandas/04_nimede_lahutamine.png)  
- Steps 5–14: [5_age.png … 14_veergude_tostmine.png](https://cs.taltech.ee/.../ex01_pandas/new/5_age.png)  

Use these to check expected column names and values if you have access.
