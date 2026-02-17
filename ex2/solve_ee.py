
import json
import re

# Questions translation map (simplified matching)
translations = {
    # Markdown
    "### Kasutusvõimalused": "### Kasutusvõimalused\n",
    "Andmestikku kasutatakse sageli:": "Andmestikku kasutatakse sageli:\n",
    "* jootraha ja arve summa seose analüüsimiseks\n": "* jootraha ja arve summa seose analüüsimiseks\n",
    "* kliendikäitumise mustrite uurimiseks\n": "* kliendikäitumise mustrite uurimiseks\n",
    "* erinevate gruppide (nt sugu, suitsetamine, nädalapäev) võrdlemiseks\n": "* erinevate gruppide (nt sugu, suitsetamine, nädalapäev) võrdlemiseks\n",
    "* visualiseerimiste ja analüüsimeetodite õppimiseks\n": "* visualiseerimiste ja analüüsimeetodite õppimiseks\n",
    "### Tunnused andmestikus": "### Tunnused andmestikus\n",
    "* **`total_bill`** – arve kogusumma dollarites\n": "* **`total_bill`** – arve kogusumma dollarites\n",
    "* **`tip`** – jäetud jootraha dollarites\n": "* **`tip`** – jäetud jootraha dollarites\n",
    "* **`sex`** – arve maksja sugu (Male, Female)\n": "* **`sex`** – arve maksja sugu (Male, Female)\n",
    "* **`smoker`** – kas klient on suitsetaja (Yes, No)\n": "* **`smoker`** – kas klient on suitsetaja (Yes, No)\n",
    "* **`day`** – nädalapäev (Thur, Fri, Sat, Sun)\n": "* **`day`** – nädalapäev (Thur, Fri, Sat, Sun)\n",
    "* **`time`** – söögiaeg (Lunch, Dinner)\n": "* **`time`** – söögiaeg (Lunch, Dinner)\n",
    "* **`size`** – inimeste arv lauas\n": "* **`size`** – inimeste arv lauas\n",
    
    # Instructions
    "Ülesande Notebook'i nimi peab olema 'EX02.ipynb'": "Ülesande Notebook'i nimi peab olema 'EX02.ipynb'",
    "See Notebook on *readonly* õigustes": "See Notebook on *readonly* õigustes",
    "Esimesed 9 on väited": "Esimesed 9 on väited",
    "iga küsimuse juures tuleb vastus lisada": "iga küsimuse juures tuleb vastus lisada",
    "Vastus peab algama": "Vastus peab algama",
    "näiteks 1. küsimuse vastus tuleb lisada muutujasse": "näiteks 1. küsimuse vastus tuleb lisada muutujasse",
    "näiteks 3. küsimuse vastus tuleb lisada muutujasse": "näiteks 3. küsimuse vastus tuleb lisada muutujasse",
    "Viimased kolm küsimust vastavalt": "Viimased kolm küsimust vastavalt",
    "Impordime andmeseti": "Impordime andmeseti",
    "Andmestik": "Andmestik",
    "sisaldab **244 vaatlust** (kirjet)": "sisaldab **244 vaatlust** (kirjet)",
    "Tee esmane analüüs andmetele": "Tee esmane analüüs andmetele",
    "Tõesta või lükka ümber": "Tõesta või lükka ümber",
    "Joonista sobiv graafik/graafikud ja vasta paari lausega": "Joonista sobiv graafik/graafikud ja vasta paari lausega",
}

# Answers in Russian (to be translated to Estonian)
answers_ru = {
    "answer_one": '"Да, так как средний чек мужчин (20.74) и медиана выше, чем у женщин (18.06)."',
    "answer_two": '"Нет, на самом деле мужчины в среднем оставляют немного больше чаевых ($3.09), чем женщины ($2.83)."',
    "answer_three": '"Да, вариативность (1.96) и медиана (3.00) чаевых у курящих немного выше, чем у некурящих (1.90 и 2.74 соответственно)."',
    "answer_four": '"Да, в субботу было больше всего чеков (87), что указывает на наибольшую посещаемость."',
    "answer_five": '"Да, коэффициент корреляции составляет 0.68, что указывает на довольно сильную положительную связь."',
    "answer_six": '"Нет, средние чаевые самые высокие в воскресенье ($3.26) и самые низкие в пятницу ($2.73), то есть они не уменьшаются постоянно."',
    "answer_seven": '"Нет, корреляция не равна 1, и на диаграмме рассеяния видны случаи, когда при меньшем счете оставлены большие чаевые."',
    "answer_eight": '"Да, так как около 89% чаевых составляют менее 5 долларов."',
    "answer_nine": '"Нет, наиболее частая сумма чаевых (мода) — 2 доллара, а медиана — 2.9 доллара."',
    "answer_general_one": '"Наблюдается дисбаланс классов: мужчин (157) почти в 2 раза больше, чем женщин (87). Некурящих (151) больше, чем курящих (93)."',
    "answer_general_two": '"Все числовые признаки положительно коррелируют. Сильнее всего связь между счетом и чаевыми (0.68), а также счетом и количеством гостей (0.60)."',
    "answer_general_three": '"Выбросы в чаевых есть, особенно в субботу (максимум 10$), где их больше всего (6). В четверг их меньше, а в пятницу и воскресенье (по методу IQR) их меньше или почти нет."'
}

# Estonian Translations of Answers
answers_ee = {
    "answer_one": 'answer_one = "Jah, kuna meeste keskmine arve (20.74) ja mediaan on kõrgemad kui naistel (18.06)."',
    "answer_two": 'answer_two = "Ei, tegelikult jätavad mehed keskmiselt veidi rohkem jootraha ($3.09) kui naised ($2.83)."',
    "answer_three": 'answer_three = "Jah, suitsetajate jootraha varieeruvus (1.96) ja mediaan (3.00) on veidi kõrgemad kui mittesuitsetajatel (1.90 ja 2.74)._"',
    "answer_four": 'answer_four = "Jah, laupäeval oli kõige rohkem arveid (87), mis viitab suurimale külastatavusele."',
    "answer_five": 'answer_five = "Jah, korrelatsioonikordaja on 0.68, mis viitab üsna tugevale positiivsele seosele."',
    "answer_six": 'answer_six = "Ei, keskmine jootraha on kõrgeim pühapäeval ($3.26) ja madalaim reedel ($2.73), seega see ei vähene pidevalt."',
    "answer_seven": 'answer_seven = "Ei, korrelatsioon ei ole 1 ja hajumisdiagrammil on näha juhtumeid, kus väiksema arve puhul on jäetud suurem jootraha."',
    "answer_eight": 'answer_eight = "Jah, kuna umbes 89% jootrahadest on alla 5 dollari."',
    "answer_nine": 'answer_nine = "Ei, kõige sagedasem jootraha summa (mood) on 2 dollarit, mediaan aga 2.9 dollarit."',
    "answer_general_one": 'answer_general_one = "Klasside vahel on tasakaalustamatus: mehi (157) on peaaegu 2 korda rohkem kui naisi (87). Mittesuitsetajaid (151) on rohkem kui suitsetajaid (93)."',
    "answer_general_two": 'answer_general_two = "Kõik arvulised tunnused on positiivses korrelatsioonis. Kõige tugevam seos on arve ja jootraha (0.68) ning arve ja külaliste arvu (0.60) vahel."',
    "answer_general_three": 'answer_general_three = "Jootrahas esineb erindeid, eriti laupäeval (maksimum 10$), kus neid on kõige rohkem (6). Neljapäeval on neid vähem, reedel ja pühapäeval (IQR meetodi järgi) vähem või peaaegu üldse mitte."'
}


with open("ex2/EX02.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        new_source = []
        for line in cell["source"]:
            translated_line = line
            
            # Fill answers and add plotting code in Estonian notebook
            filled = False
            for var_name, answer_code in answers_ee.items():
                if var_name in line and "=" in line and not line.strip().startswith("#"):
                     # Replace line with answer
                     translated_line = answer_code + "\n"
                     
                     # Add plotting code (same logic as RU)
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
            
            # If not filled, check placeholder replacement (just in case, though EE nb has 'põhjendus' already)
            if not filled:
                 pass # No specific placeholder replacement needed for EE beyond standard flow

            new_source.append(translated_line)
        cell["source"] = new_source

with open("ex2/EX02.ipynb", "w") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
