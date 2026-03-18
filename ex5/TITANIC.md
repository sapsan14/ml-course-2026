Titanic Disaster
Completion requirements
To do: Complete the activity
Eesmärk
Luua logistilise regressiooni mudel ennustamaks, kas reisija elas Titanicu õnnetuse üle või mitte.

Andmestiku link: Kaggle - Titanic https://www.kaggle.com/datasets/yasserh/titanic-dataset

Andmekogum sisaldab teavet ellujäänute ja Titanicul hukkunute kohta.

Ülesanne
Andme analüüs

Laadige alla andmestik, uurige selle põhistatistikat ja struktuuri.
Mõista iga muutuja tähendust, tuvasta regressiooni sihtmuutuja.
(Hint: Survived)

Andmete eeltöötlus:

Kontrolli puuduvaid väärtusi ja vajadusel kasuta nende käsitlemiseks sobivaid tehnikaid.
Uuri sihtmuutuja (Survived) jaotust. Vajadusel rakenda jaotuse normaliseerimiseks teisendusi.
Tuvasta andmekogus kõik võimalikud kõrvalekalded ja vajadusel käsitle neid.
Tunnuste uurimine ja valik:

Analüüsi sihtmuutuja ja muude tunnuste vahelist seost korrelatsioonianalüüsi ja hajuvusdiagrammide abil.
Vali sihtmuutuja ennustamiseks asjakohased tunnused. Põhjenda oma tunnuste valikut hiljem raportis.
Vajadusel loo uusi tunnuseid.
Mudeli treenimine:

Jaga andmekogum treening- ja testimiskomplektideks.
Standardiseeri tunnused sobivate skaleerimistehnikate abil.
Koosta vähemalt kaks erinevat regressioonimudelit (nt kasutades erinevaid tunnuseid.
Mudeli hindamine:

Hinda oma mudelite toimivust sobivate mõõdikute (nt f1, accuracy, recall) abil.
Võrdle mudelite toimivust ja analüüsi täheldatud erinevusi.
Esita:

Jagatud Jupyteri notebook, mis sisaldab kogu koodi (jäta käivitamise tulemused ka alles), kommentaare ja analüüsi.
Faili nimi peaks olema - EX05_titanic_disaster_prediction.ipynb.
Notebook-i kood ei tohi sisaldada automaatse testeri peal käivitamisel vigu.
Kirjuta lühike kokkuvõte oma töö peamistest järeldustest (Notebook-is, teksti blokina, 8-20 lauset). Nt. tee ülevaade sellest, kuidas erinevad tunnused mõjutavad eluaseme hindu.
Testimine:

Testeri peal on toetatud järgmised välised teegid: numpy, pandas, seaborn, matplotlib, sklearn. Koodi kontrollimiseks eeldab tester mallis toodud muutujate olemasolu.

Mall:

import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt

# Ülesande eesmärk:
# Luua logistilise regressiooni mudel, mis ennustab,
# kas reisija elas Titanicu õnnetuse üle.

# Üldised juhised:
# - Kasuta scikit-learn’i mudeleid ja tööriistu
# - Algoritme ei ole vaja implementeerida nullist
# - Tunnuste valik ja eeltöötlus peavad olema põhjendatud


# 1. Andmestiku laadimine
# Laadi Titanicu andmestik ja uuri selle struktuuri ning
# põhilisi statistilisi näitajaid.
# Tuvasta sihtmuutuja.

if 'google.colab' in sys.modules:
    from google.colab import drive
    drive.mount('/content/drive')
    path = '/content/drive/MyDrive/google_colab/Titanic-Dataset.csv'
else:
    path = 'Titanic-Dataset.csv'

data = pd.read_csv(path)

target = '?'


# 2. Andmete eeltöötlus
# Kontrolli:
# - puuduvaid väärtusi
# - vigaseid või ebamõistlikke väärtusi
# Vajadusel:
# - täida puuduvaid väärtusi (nt SimpleImputer)
# - kodeeri kategoorilised tunnused
# - eemalda mittevajalikud veerud

# TODO: andmete puhastamine ja ettevalmistamine


# 3. Tunnuste uurimine ja valik
# Analüüsi sihtmuutuja ja teiste tunnuste seoseid:
# - korrelatsioonid
# - jaotused
# - visualiseeringud
#
# Vali tunnused, mida kasutad mudeli treenimiseks.
# Valik peab olema põhjendatud.

selected_features = []


# 4. Treening- ja testandmete jagamine
# Jaga andmestik treening- ja testkomplektideks.

X = None 
y = None

X_train = None
X_test = None
y_train = None
y_test = None


# 5. Andmete skaleerimine
# Skaleeri tunnused, et parandada mudeli stabiilsust.
# Kasuta MinMaxScaler-it.
# NB! Pärast X_train, X_test skaleerimist, skaleerige ka muutuja X. See on vajalik testidel võrdluseks.


# 6. Mudelite treenimine
# Treeni vähemalt kaks erinevat logistilise regressiooni mudelit

model_1 = None
model_2 = None


# 7. Mudelite hindamine
# Hinda mudeleid kasutades sobivaid mõõdikuid:
# - accuracy
# - precision
# - recall
# - f1-score
# - auc-roc
#
# Võrdle tulemusi ja analüüsi erinevusi. Kasuta scikit-learn'i.

model_1_predictions = None
model_2_predictions = None

models = [] # [(mudel1, f1-score), (mudel2, f1-score)]


# 8. Kokkuvõte
# Kirjuta lühike kokkuvõte (8–20 lauset), kus:
# - kirjeldad andmestiku peamisi mustreid
# - selgitad, millised tunnused mõjutavad ellujäämist
# - võrdled mudeleid mõõdikute põhjal
# - teed järeldused mudelite sobivuse kohta

summary = ""