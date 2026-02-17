import json

# Translation map
translations = {
    # Markdown translations
    "EX03 - Täiskasvanute sissetulek": "EX03 - Доход взрослых",
    "Ülesande Notebook'i nimi peab olema 'EX03_adults.ipynb'": "Имя Notebook должно быть 'EX03_adults.ipynb'",
    "See Notebook on readonly õigustes": "Этот Notebook в режиме *readonly*, сделайте копию: File --> Save a copy in Drive",
    "## 1) Andmete laadimine": "## 1) Загрузка данных",
    "Määra `adult.data` faili asukoht ja veergude nimed vastavalt algsele andmestikule.": "Укажите путь к файлу `adult.data` и имена столбцов согласно исходному набору данных.",
    "veebilehelt, kust andmestik alla laaditi": "с веб-сайта, откуда был загружен набор данных",
    "Failis ja veebilehel on mõnes nimes sidekriips": "В файле и на веб-сайте в некоторых названиях есть дефис",
    "Sinu ülesanne:** täida allolev": "**Ваша задача:** заполните список",
    "Kontrolli:**": "**Проверка:**",
    "## 2) Puuduvate väärtuste käsitlemine": "## 2) Обработка пропущенных значений",
    "Mõnes kategoorilises veerus on puuduvaid väärtusi kujul": "В некоторых категориальных столбцах есть пропущенные значения в виде",
    "eemaldada või käsitleda ebaõigeid väärtusi": "удалить или обработать некорректные значения",
    "Asendame need `NaN`-idega": "Заменим их на `NaN`",
    "ja eemaldame read, kus esineb puuduvaid väärtusi": "и удалим строки с пропущенными значениями",
    "(lihtne esmane lähenemine uuriva andmeanalüüsi jaoks)": "(простой первичный подход для исследовательского анализа)",
    ", et analüüs oleks usaldusväärne.": ", чтобы анализ был надежным.",
    "annab pärast puhastamist kõikjal 0.": "после очистки возвращает везде 0.",
    "Salvesta muutujatesse ridade arv enne ja pärast puhastamist": "Сохраните количество строк до и после очистки в переменные",
    "ning võrdle neid.": "и сравните их.",
    
    "## 3) Binaarne tuluveeru versioon": "## 3) Бинарная версия столбца дохода",
    "Loome `income_binary`": "Создаем `income_binary`",
    "1, kui `income` on `>50K`": "1, если `income` >50K",
    "0, vastasel juhul": "0 в противном случае",
    "luua uus veerg": "создать новый столбец",
    "ja kontrollida, et väärtused on ainult 0/1.": "и проверить, что значения только 0/1.",
    
    "## 4) Lihtsad andmeanalüüsi ülesanded": "## 4) Простые задачи анализа данных",
    "Selles osas harjutad andmete uurimist": "В этой части вы попрактикуетесь в исследовании данных",
    "arvuta allpool toodud väärtused": "вычислите приведенные ниже значения",
    "Pandase abil ning salvestad tulemused muutujatesse.": "с помощью Pandas и сохраните результаты в переменные.",
    "ja salvesta need vastavatesse muutujatesse.": "и сохраните их в соответствующие переменные.",
    
    "## 5) Visualiseerimine": "## 5) Визуализация",
    "Koosta järgmised graafikud": "Постройте следующие графики",
    "Vanuse jaotus (histogramm)": "Распределение возраста (гистограмма)",
    "Keskmised töötunnid ametite lõikes": "Средние рабочие часы по профессиям",
    "Numbriliste tunnuste korrelatsioonimaatriks": "Корреляционная матрица числовых признаков",
    "Töötundide jaotus soo lõikes": "Распределение рабочих часов по полу",
    "Vanus tulugruppide lõikes": "Возраст по группам дохода",
    "Kõigil graafikutel on pealkiri": "У всех графиков есть заголовок",
    "ja telgede sildid.": "и подписи осей.",
    "Korrelatsioonimaatriks kasutab ainult sobivaid numbrilisi veerge.": "Матрица корреляции использует только подходящие числовые столбцы.",
    "Vihje:* vajadusel tee kategooriate telje sildid loetavaks": "Подсказка:* при необходимости сделайте подписи категорий читаемыми",
    
    "## 6) Salvesta tabel tagasi csv kujule": "## 6) Сохраните таблицу обратно в CSV",
    "Viimase sammuna salvestame": "В качестве последнего шага сохраняем",
    "puhastatud ja töödeldud andmestiku CSV-faili.": "очищенный и обработанный набор данных в CSV-файл.",

    # Additional details
    "**Märkus veerunimede kohta:**": "**Примечание по именам столбцов:**",
    "Veerunimed saad võtta kas:": "Имена столбцов можно взять либо:",
    "(nt UCI Machine Learning Repository)": "(например, UCI Machine Learning Repository)",
    "või `adult.names` faili lõpust, mis on allalaaditud andmestikuga samas kaustas.": "или из конца файла `adult.names`, который находится в той же папке.",
    "Kuna Pythonis veerunimed ei tohi sisaldada sidekriipse, tuleb need asendada alakriipsudega:": "Поскольку в Python имена столбцов не могут содержать дефисы, их нужно заменить подчеркиваниями:",
    "näiteks": "например",
    "järjend sobivate veerunimedega,": "списком подходящих имен столбцов,",
    "kasutades `adult.names` faili või veebilehel toodud infot.": "используя файл `adult.names` или информацию с веб-сайта.",
    "Andmestikul on 15 veergu.": "В наборе данных 15 столбцов.",
    "kuvab eelduspäraseid veerge ja väärtusi.": "отображает ожидаемые столбцы и значения.",
    "Vihje:": "Подсказка:",
    "tee sellest endale koopia File --> Save a copy in Drive": "сделайте копию: File --> Save a copy in Drive",
    
    # Code comment translations
    "# Mitu naist teenib rohkem kui 50K?": "# Сколько женщин зарабатывают более 50K?",
    "# Mitu meest teenib rohkem kui 50K?": "# Сколько мужчин зарабатывают более 50K?",
    "# Mitu inimest kokku teenib rohkem kui 50K?": "# Сколько всего людей зарабатывают более 50K?",
    "# Kui suur protsent naistest teenib rohkem kui 50K?": "# Какой процент женщин зарабатывает более 50K?",
    "# Kui suur protsent meestest teenib rohkem kui 50K?": "# Какой процент мужчин зарабатывает более 50K?",
    "# Milline on keskmine vanus inimeste seas, kes teenivad rohkem kui 50K?": "# Каков средний возраст людей, зарабатывающих более 50K?",
    "# Milline on keskmine vanus inimeste seas, kes teenivad kuni 50K?": "# Каков средний возраст людей, зарабатывающих до 50K?",
    "# Kuvame tulemused": "# Выводим результаты",
    "# Vanuse jaotus (histogramm)": "# Распределение возраста (гистограмма)",
    "# Keskmised töötunnid ametite lõikes (tulpdiagramm)": "# Средние рабочие часы по профессиям (столбчатая диаграмма)",
    "# Korrelatsioonid arvuliste tunnuste vahel": "# Корреляции между числовыми признаками",
    "# Töötundide jaotus soo lõikes": "# Распределение рабочих часов по полу",
    "# Vanus tulugruppide lõikes": "# Возраст по группам дохода"
}

# Code injections
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

# Visualization codes
viz1_code = """
# Vanuse jaotus (histogramm)
# Распределение возраста (гистограмма)
plt.figure(figsize=(10, 6))
sns.histplot(df_viz['age'], bins=20, kde=True)
plt.title('Распределение возраста / Age Distribution')
plt.xlabel('Возраст / Age')
plt.ylabel('Количество / Count')
plt.show()
"""

viz2_code = """
# Keskmised töötunnid ametite lõikes (tulpdiagramm)
# Средние рабочие часы по профессиям (столбчатая диаграмма)
plt.figure(figsize=(12, 6))
df_viz.groupby('occupation')['hours_per_week'].mean().sort_values().plot(kind='bar')
plt.title('Средние рабочие часы по профессиям / Avg hours by occupation')
plt.xlabel('Профессия / Occupation')
plt.ylabel('Часы в неделю / Hours per week')
plt.xticks(rotation=90)
plt.show()
"""

viz3_code = """
# Korrelatsioonid arvuliste tunnuste vahel (sh income_binary)
# Корреляции между числовыми признаками (включая income_binary)
plt.figure(figsize=(10, 8))
# Select only numeric columns for correlation
numeric_df = df_viz.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Корреляционная матрица / Correlation Matrix')
plt.show()
"""

viz4_code = """
# Töötundide jaotus soo lõikes
# Распределение рабочих часов по полу
plt.figure(figsize=(10, 6))
sns.histplot(data=df_viz, x='hours_per_week', hue='sex', multiple='stack', bins=20)
plt.title('Распределение рабочих часов по полу / Hours per week by Sex')
plt.xlabel('Часы в неделю / Hours per week')
plt.ylabel('Количество / Count')
plt.show()
"""

viz5_code = """
# Vanus tulugruppide lõikes (viiuldiagramm) - kasuta `income_binary`
# Возраст по группам дохода
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_viz, x='income_binary', y='age')
plt.title('Возраст по группам дохода / Age by Income Group')
plt.xlabel('Доход >50K (0=Нет, 1=Да)')
plt.ylabel('Возраст / Age')
plt.show()
"""

with open("ex3/EX03_adults.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    # Translate Markdown
    if cell["cell_type"] == "markdown":
        new_source = []
        for line in cell["source"]:
            translated_line = line
            for est, rus in translations.items():
                if est in translated_line:
                    translated_line = translated_line.replace(est, rus)
            new_source.append(translated_line)
        cell["source"] = new_source

    # Translate Comments & Inject Code
    if cell["cell_type"] == "code":
        source_text = "".join(cell["source"])
        
        # Inject Column Names
        if "column_names =" in source_text and "'?'" in source_text:
            # We preserve the top part of the cell if it has imports or path setup?
            # actually the cell has 'if "google.colab" ...' then 'column_names = [...]'
            # We want to keep the file loading part but replace the list.
            # Simpler: replace the list content specifically.
             pass # We will do a full replacement for this block logic below

        new_source = []
        # Since we are iterating lines, we need state or clever replacement.
        # Let's replace the whole source if it matches a pattern.
        
        if "column_names = [" in source_text and "'?'" in source_text:
            # This is the loading cell.
            # We will keep the top part (colab check) but replace column_names and the read_csv part (to ensure it works)
            # Actually, reading the file is fine if column_names is correct.
            # Let's just reconstruct the cell.
            original_lines = cell["source"]
            # Find where column_names starts
            start_idx = -1
            for i, line in enumerate(original_lines):
                 if "column_names = [" in line:
                     start_idx = i
                     break
            
            if start_idx != -1:
                 # Keep everything before column_names
                 new_source = original_lines[:start_idx]
                 # Add new column names
                 new_source.append(column_names_code.strip() + "\n\n")
                 
                 # Add the read_csv line (it was at the end)
                 # We skip the original list lines until we hit ']'
                 end_idx = -1
                 for i in range(start_idx, len(original_lines)):
                     if "]" in original_lines[i]:
                         end_idx = i
                         break
                 
                 if end_idx != -1:
                      # Append the rest after the list
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
        
        else:
             # Just translate comments
             new_source = []
             for line in cell["source"]:
                 translated_line = line
                 for est, rus in translations.items():
                     if est in translated_line:
                         translated_line = translated_line.replace(est, rus)
                 new_source.append(translated_line)
             cell["source"] = new_source

with open("ex3/EX03_adults_RU.ipynb", "w") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
