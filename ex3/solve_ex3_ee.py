
import json

# Code injections in Estonian (no string translation needed, just functional)
column_names_code = """
column_names = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"
]
"""

cleaning_code = """
df_clean = df_raw.copy()
# Replace ? with NaN
df_clean.replace('?', np.nan, inplace=True)
# Drop NaNs
df_clean.dropna(inplace=True)
rows_before = df_raw.shape[0]
rows_after = df_clean.shape[0]
print(f"Rows before: {rows_before}, Rows after: {rows_after}")
"""

binary_income_code = """
df_model = df_clean.copy()
# Create binary income: 1 if >50K, 0 otherwise
# Note: Data might have leading spaces, so strip
df_model['income_binary'] = (df_model['income'].str.strip() == '>50K').astype(int)
print(df_model['income_binary'].value_counts())
"""

analysis_code = """
df_analysis = df_model.copy()

# 4.1 Number of females > 50K
female_over_50k = df_analysis[(df_analysis['sex'].str.strip() == 'Female') & (df_analysis['income_binary'] == 1)].shape[0]

# 4.2 Number of males > 50K
male_over_50k = df_analysis[(df_analysis['sex'].str.strip() == 'Male') & (df_analysis['income_binary'] == 1)].shape[0]

# 4.3 Total > 50K
total_over_50k = df_analysis[df_analysis['income_binary'] == 1].shape[0]

# 4.4 % females > 50K
females = df_analysis[df_analysis['sex'].str.strip() == 'Female']
female_over_50k_pct = (female_over_50k / len(females)) * 100 if len(females) > 0 else 0

# 4.5 % males > 50K
males = df_analysis[df_analysis['sex'].str.strip() == 'Male']
male_over_50k_pct = (male_over_50k / len(males)) * 100 if len(males) > 0 else 0

# 4.6 Avg age > 50K
avg_age_over_50k = df_analysis[df_analysis['income_binary'] == 1]['age'].mean()

# 4.7 Avg age <= 50K
avg_age_under_50k = df_analysis[df_analysis['income_binary'] == 0]['age'].mean()

# Kuvame tulemused
print(f"Female >50K: {female_over_50k}")
print(f"Male >50K: {male_over_50k}")
print(f"Total >50K: {total_over_50k}")
print(f"Female >50K %: {female_over_50k_pct:.2f}%")
print(f"Male >50K %: {male_over_50k_pct:.2f}%")
print(f"Avg age >50K: {avg_age_over_50k:.2f}")
print(f"Avg age <=50K: {avg_age_under_50k:.2f}")
"""

# Visualization codes (Titles in Estonian)
viz1_code = """
df_viz = df_analysis.copy()

# Vanuse jaotus (histogramm)
plt.figure(figsize=(10, 6))
sns.histplot(df_viz['age'], bins=20, kde=True)
plt.title('Vanuse jaotus / Age Distribution')
plt.xlabel('Vanus / Age')
plt.ylabel('Kogus / Count')
plt.show()
"""

viz2_code = """
# Keskmised töötunnid ametite lõikes (tulpdiagramm)
plt.figure(figsize=(12, 6))
df_viz.groupby('occupation')['hours_per_week'].mean().sort_values().plot(kind='bar')
plt.title('Keskmised töötunnid ametite lõikes / Avg hours by occupation')
plt.xlabel('Amet / Occupation')
plt.ylabel('Tunde nädalas / Hours per week')
plt.xticks(rotation=90)
plt.show()
"""

viz3_code = """
# Korrelatsioonid arvuliste tunnuste vahel (sh income_binary)
plt.figure(figsize=(10, 8))
# Select only numeric columns for correlation
numeric_df = df_viz.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korrelatsioonimaatriks / Correlation Matrix')
plt.show()
"""

viz4_code = """
# Töötundide jaotus soo lõikes
plt.figure(figsize=(10, 6))
sns.histplot(data=df_viz, x='hours_per_week', hue='sex', multiple='stack', bins=20)
plt.title('Töötundide jaotus soo lõikes / Hours per week by Sex')
plt.xlabel('Tunde nädalas / Hours per week')
plt.ylabel('Kogus / Count')
plt.show()
"""

viz5_code = """
# Vanus tulugruppide lõikes (viiuldiagramm) - kasuta `income_binary`
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_viz, x='income_binary', y='age')
plt.title('Vanus tulugruppide lõikes / Age by Income Group')
plt.xlabel('Sissetulek >50K (0=Ei, 1=Jah)')
plt.ylabel('Vanus / Age')
plt.show()
"""

with open("ex3/EX03_adults.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    # No markdown translation loops needed for the original Estonian file.

    # Inject Code
    if cell["cell_type"] == "code":
        source_text = "".join(cell["source"])

        # Inject Column Names
        if "column_names = [" in source_text and "'?'" in source_text:
            original_lines = cell["source"]
            start_idx = -1
            for i, line in enumerate(original_lines):
                 if "column_names = [" in line:
                     start_idx = i
                     break
            if start_idx != -1:
                 new_source = original_lines[:start_idx]
                 new_source.append(column_names_code.strip() + "\n\n")
                 end_idx = -1
                 for i in range(start_idx, len(original_lines)):
                     if "]" in original_lines[i]:
                         end_idx = i
                         break
                 if end_idx != -1:
                      new_source.extend(original_lines[end_idx+1:])
            else:
                 new_source = original_lines
            cell["source"] = new_source

        elif "df_clean = df_raw.copy()" in source_text:
            cell["source"] = [cleaning_code.strip()]

        elif "df_model = df_clean.copy()" in source_text:
             cell["source"] = [binary_income_code.strip()]

        elif "df_analysis = df_model.copy()" in source_text:
             cell["source"] = [analysis_code.strip()]

        elif "# Vanuse jaotus (histogramm)" in source_text:
             cell["source"] = [viz1_code.strip()]

        elif "# Keskmised töötunnid ametite lõikes" in source_text:
             cell["source"] = [viz2_code.strip()]

        elif "# Korrelatsioonid arvuliste tunnuste vahel" in source_text:
             cell["source"] = [viz3_code.strip()]

        elif "# Töötundide jaotus soo lõikes" in source_text:
             cell["source"] = [viz4_code.strip()]

        elif "# Vanus tulugruppide lõikes" in source_text:
             cell["source"] = [viz5_code.strip()]

with open("ex3/EX03_adults.ipynb", "w") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
