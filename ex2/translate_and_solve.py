
import json
import re

# Answers
answers = {
    "answer_one": 'answer_one = "Да, так как средний чек мужчин (20.74) и медиана выше, чем у женщин (18.06)."',
    "answer_two": 'answer_two = "Нет, на самом деле мужчины в среднем оставляют немного больше чаевых ($3.09), чем женщины ($2.83)."',
    "answer_three": 'answer_three = "Да, вариативность (1.96) и медиана (3.00) чаевых у курящих немного выше, чем у некурящих (1.90 и 2.74 соответственно)."',
    "answer_four": 'answer_four = "Да, в субботу было больше всего чеков (87), что указывает на наибольшую посещаемость."',
    "answer_five": 'answer_five = "Да, коэффициент корреляции составляет 0.68, что указывает на довольно сильную положительную связь."',
    "answer_six": 'answer_six = "Нет, средние чаевые самые высокие в воскресенье ($3.26) и самые низкие в пятницу ($2.73), то есть они не уменьшаются постоянно."',
    "answer_seven": 'answer_seven = "Нет, корреляция не равна 1, и на диаграмме рассеяния видны случаи, когда при меньшем счете оставлены большие чаевые."',
    "answer_eight": 'answer_eight = "Да, так как около 89% чаевых составляют менее 5 долларов."',
    "answer_nine": 'answer_nine = "Нет, наиболее частая сумма чаевых (мода) — 2 доллара, а медиана — 2.9 доллара."',
    "answer_general_one": 'answer_general_one = "Наблюдается дисбаланс классов: мужчин (157) почти в 2 раза больше, чем женщин (87). Некурящих (151) больше, чем курящих (93)."',
    "answer_general_two": 'answer_general_two = "Все числовые признаки положительно коррелируют. Сильнее всего связь между счетом и чаевыми (0.68), а также счетом и количеством гостей (0.60)."',
    "answer_general_three": 'answer_general_three = "Выбросы в чаевых есть, особенно в субботу (максимум 10$), где их больше всего (6). В четверг их меньше, а в пятницу и воскресенье (по методу IQR) их меньше или почти нет."'
}

# Questions translation map (simplified matching)
translations = {
    "Meeste arved on naiste omadest suuremad": "Счета мужчин больше, чем у женщин",
    "Meeste keskmine arve suurus on suurem kui naistel": "Средний счет мужчин больше, чем у женщин",
    "Naised jätavad keskmiselt rohkem jootraha kui mehed": "Женщины в среднем оставляют больше чаевых, чем мужчины",
    "Kas suitsetajate ja mittesuitsetajate jootraha varieeruvus ja mediaan erinevad?": "Отличаются ли вариативность и медиана чаевых у курящих и некурящих?",
    "Laupäeval on kõige rohkem külastajaid": "В субботу больше всего посетителей",
    "Arve suuruse ja jootraha vahel on tugev positiivne korrelatsioon": "Существует сильная положительная корреляция между суммой счета и чаевыми",
    "Keskmine jootraha väheneb nädala kulgedes": "Средние чаевые уменьшаются в течение недели",
    "Suurem arve tähendab alati suuremat jootraha": "Больший счет всегда означает большие чаевые",
    "Enamik jootrahadest on väiksem kui 5 dollarit": "Большинство чаевых меньше 5 долларов",
    "Enamus ajast jäetakse jootraha umbes 4 dollarit": "Чаще всего оставляют около 4 долларов чаевых",
    "Üldised küsimused": "Общие вопросы",
    "Mida oskad öelda erinevate klasside võrdsuse kohta? Võta näiteks sugu ja suitsetajad/ mittesuitsetajad.": "Что можно сказать о равенстве классов? Например, пол и курение.",
    "Mida oskad öelda tunnuste korrelatsiooni kohta?": "Что можно сказать о корреляции признаков?",
    "Kas jootraha suurus sisaldab erindeid ja kuidas need erinevad nädalapäevade lõikes?": "Есть ли выбросы в размере чаевых и как они различаются по дням недели?"
}

with open("ex2/EX02.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    # Translate Markdown
    if cell["cell_type"] == "markdown":
        new_source = []
        for line in cell["source"]:
            translated_line = line
            # Simple substring replacement for titles
            for est, rus in translations.items():
                if est in translated_line:
                    translated_line = translated_line.replace(est, rus)
            
            if "### Kasutusvõimalused" in translated_line:
                translated_line = "### Возможности использования\n"

            if "Andmestikku kasutatakse sageli:" in translated_line:
                translated_line = "Этот набор данных часто используется для:\n"

            if "* jootraha ja arve summa seose analüüsimiseks" in translated_line:
                translated_line = "* анализа связи между суммой чека и чаевыми\n"
            if "* kliendikäitumise mustrite uurimiseks" in translated_line:
                translated_line = "* изучения паттернов поведения клиентов\n"
            if "* erinevate gruppide (nt sugu, suitsetamine, nädalapäev) võrdlemiseks" in translated_line:
                translated_line = "* сравнения различных групп (например, по полу, курению, дням недели)\n"
            if "* visualiseerimiste ja analüüsimeetodite õppimiseks" in translated_line:
                translated_line = "* изучения методов визуализации и анализа\n"
            if "### Tunnused andmestikus" in translated_line:
                translated_line = "### Признаки в наборе данных\n"
            if "* **`total_bill`** – arve kogusumma dollarites" in translated_line:
                translated_line = "* **`total_bill`** – общая сумма чека в долларах\n"
            if "* **`tip`** – jäetud jootraha dollarites" in translated_line:
                translated_line = "* **`tip`** – оставленные чаевые в долларах\n"
            if "* **`sex`** – arve maksja sugu (Male, Female)" in translated_line:
                translated_line = "* **`sex`** – пол плательщика (Male, Female)\n"
            if "* **`smoker`** – kas klient on suitsetaja (Yes, No)" in translated_line:
                translated_line = "* **`smoker`** – курит ли клиент (Yes, No)\n"
            if "* **`day`** – nädalapäev (Thur, Fri, Sat, Sun)" in translated_line:
                translated_line = "* **`day`** – день недели (Thur, Fri, Sat, Sun)\n"
            if "* **`time`** – söögiaeg (Lunch, Dinner)" in translated_line:
                translated_line = "* **`time`** – время приема пищи (Lunch, Dinner)\n"
            if "* **`size`** – inimeste arv lauas" in translated_line:
                translated_line = "* **`size`** – количество людей за столом\n"
            
            # Additional manual translations for instructions

            if "Ülesande Notebook'i nimi peab olema" in translated_line:
                translated_line = "- **Имя Notebook должно быть 'EX02.ipynb'**\n"
            if "See Notebook on *readonly* õigustes" in translated_line:
                translated_line = "- **Этот Notebook в режиме *readonly*, сделайте копию: File --> Save a copy in Drive**"
            if "Esimesed 9 on väited" in translated_line:
                translated_line = "- Первые 9 — это утверждения, которые нужно подтвердить или опровергнуть\n"
            if "iga küsimuse juures tuleb vastus lisada" in translated_line:
                translated_line = "  - ответ нужно записать в переменную\n"
            if "Vastus peab algama" in translated_line:
                translated_line = "  - Ответ должен начинаться с 'Да' или 'Нет'\n"
            if "näiteks 1. küsimuse vastus tuleb lisada muutujasse" in translated_line:
                translated_line = "  - например, ответ на 1-й вопрос нужно добавить в переменную `answer_one = \"Да/Нет, потому что ...\"`\n"
            if "näiteks 3. küsimuse vastus tuleb lisada muutujasse" in translated_line:
                translated_line = "  - например, ответ на 3-й вопрос нужно добавить в переменную `answer_three = \"Да/Нет, потому что ...\"`\n"
            if "Viimased kolm küsimust vastavalt" in translated_line:
                translated_line = "  - Последние три вопроса соответственно:\n"
            if "põhjendus" in translated_line and "answer_general" in translated_line:
                 translated_line = translated_line.replace("põhjendus", "обоснование")
            if "Impordime andmeseti" in translated_line:
                translated_line = "# Импортируем датасет \"tips\"\n"
            if "Andmestik" in translated_line and "on väike ja tuntud" in translated_line:
                translated_line = "Набор данных **`tips`** — это классический пример для обучения анализу данных.\n"
            if "sisaldab **244 vaatlust** (kirjet)" in translated_line:
                translated_line = "Набор содержит **244 наблюдения** (записи), где каждая запись представляет одно посещение ресторана. Для каждого наблюдения сохранены как числовые, так и категориальные признаки, что позволяет проводить разнообразный статистический анализ.\n"
            if "Tee esmane analüüs andmetele" in translated_line:
                translated_line = "# Сделайте первичный анализ данных"
            if "Tõesta või lükka ümber" in translated_line:
                translated_line = "# Подтверди или опровергни: используй график как доказательство"
            if "Joonista sobiv graafik/graafikud ja vasta paari lausega" in translated_line:
                translated_line = "# Нарисуй график и ответь парой предложений\n"
            if "Mida oskad öelda erinevate klasside võrdsuse kohta? Võta näiteks sugu ja suitsetajad/ mittesuitsetajad." in translated_line:
                translated_line = "## 1\\. Что можно сказать о равенстве классов? (Например, пол и курение)"
            if "Mida oskad öelda tunnuste korrelatsiooni kohta?" in translated_line:
                translated_line = "## 2\\. Что можно сказать о корреляции признаков?"
            if "Kas jootraha suurus sisaldab erindeid ja kuidas need erinevad nädalapäevade lõikes?" in translated_line:
                translated_line = "## 3\\. Есть ли выбросы в размере чаевых и как они различаются по дням недели?"

            new_source.append(translated_line)
        cell["source"] = new_source

    # Translate Code comments
    if cell["cell_type"] == "code":
        new_source = []
        for line in cell["source"]:
            translated_line = line
            # Just translate comments, do not solve
            if "# Väide:" in line:
                for est, rus in translations.items():
                    if est in line:
                         translated_line = f"# Утверждение: {rus}\n"
            if "# Vata:" in line or "# Vasta:" in line:
                for est, rus in translations.items():
                     if est in line:
                         translated_line = f"# Вопрос: {rus}\n"
            if "# Joonista sobiv graafik" in line:
                 translated_line = "# Нарисуй подходящий график и посмотри, верно ли утверждение\n"
            if "# Alusta vastust" in line:
                 translated_line = "# Начни ответ с подтверждения или опровержения\n"
            if "# Näiteks:" in line:
                 translated_line = "# Пример: answer_one = \"Нет, потому что ...\"\n"
            # Check if we should fill the answer
            filled = False
            for var_name, answer_code in answers.items():
                if var_name in line and "=" in line and not line.strip().startswith("#"):
                     # Add plotting code before the answer if it's a specific question
                     # This is tricky without parsing. I will just replace the answer line.
                     translated_line = answer_code + "\n"
                     
                     # Add visualization code based on variable name
                     plot_code = ""
                     if var_name == "answer_one":
                         plot_code = "sns.boxplot(data=df, x='sex', y='total_bill')\nplt.show()\n"
                     elif var_name == "answer_two":
                         plot_code = "sns.boxplot(data=df, x='sex', y='tip')\nplt.show()\n"
                     elif var_name == "answer_three":
                         plot_code = "sns.boxplot(data=df, x='smoker', y='tip')\nplt.show()\n"
                     elif var_name == "answer_four":
                         plot_code = "sns.countplot(data=df, x='day')\nplt.show()\n"
                     elif var_name == "answer_five":
                         plot_code = "sns.scatterplot(data=df, x='total_bill', y='tip')\nplt.show()\n"
                     elif var_name == "answer_six":
                         plot_code = "sns.lineplot(data=df, x='day', y='tip', errorbar=None)\nplt.show()\n"
                     elif var_name == "answer_seven":
                         plot_code = "sns.scatterplot(data=df, x='total_bill', y='tip')\nplt.show()\n"
                     elif var_name == "answer_eight":
                         plot_code = "sns.histplot(data=df, x='tip', bins=20)\nplt.axvline(5, color='red')\nplt.show()\n"
                     elif var_name == "answer_nine":
                         plot_code = "sns.histplot(data=df, x='tip', bins=20)\nplt.axvline(4, color='red')\nplt.show()\n"
                     elif var_name == "answer_general_one":
                         plot_code = "sns.countplot(data=df, x='sex', hue='smoker')\nplt.show()\n"
                     elif var_name == "answer_general_two":
                         plot_code = "sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')\nplt.show()\n"
                     elif var_name == "answer_general_three":
                         plot_code = "sns.boxplot(data=df, x='day', y='tip')\nplt.show()\n"

                     if plot_code:
                         new_source.append(plot_code)
                     
                     filled = True
                     break

            if not filled:
                 if 'answer_' in translated_line and 'sest' in translated_line:
                     translated_line = translated_line.replace('..., sest ...', '..., потому что ...')
                     translated_line = translated_line.replace('põhjendus ...', 'обоснование ...')
                     translated_line = translated_line.replace('põhjendus', 'обоснование')

            new_source.append(translated_line)
        cell["source"] = new_source

with open("ex2/EX02_RU.ipynb", "w") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
