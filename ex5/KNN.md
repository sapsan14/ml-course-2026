KNN
Completion requirements
To do: Complete the activity
Eesmärk
Rakendada k-lähimate naabrite (KNN) klassifikaatorit rinnavähi diagnostika andmestikul ning hinnata mudeli võimet tuvastada pahaloomulisi kasvajaid.

Andmekogum sisaldab teavet erinevate tunnuste kohta, mis kirjeldavad rinnavähi näidiseid ning klassi (malignant vs benign).

Ülesanne
Andmete ettevalmistus:

Laadi andmestik kasutades load_breast_cancer() meetodit ja salvesta toorandmed muutujatesse X, y, feature_names, target_names.
Koosta pandas DataFrame df ja lisa veerg klass, kus väärtused on tekstilised (malignant, benign).
Uuri DataFrame struktuuri: andmetüüpe, väärtuste jaotusi ja puuduvaid andmeid.
Jaga andmed treening- ja testkomplektideks (test_size=0.2, random_state=42, stratify=y) ja salvesta need X_train, X_test, y_train, y_test.
Skaleerimine ja modelleerimine:

Standardiseeri tunnused kasutades StandardScaler-it, luues X_train_scaled ja X_test_scaled.
Implementeeri funktsioonid my_knn_predict_single ja my_knn_predict, mis kasutavad eukleidilist kaugust ja collections.Counter enamus-hääletust.
Ennusta testkomplekti punktide klassid ja arvuta recall_score pahaloomulise klassi (label=0) jaoks.
Analüüs:

Kirjelda, kuidas skaleerimine mõjutab tunnuste jaotusi ja miks see on KNN puhul oluline.
Kommenteeri, milline k väärtus andis parima tulemuse ja kuidas see mõjutab bias/variance kompromissi.
(Vabatahtlik) Lisa visualiseerimine (nt tunnuse histogramm või kaugusjaotus) oma järelduste toetamiseks.
Esita:

Lõplik lahendus peab olema Jupyter Notebook nimega EX06_KNN.ipynb, mis sisaldab kogu koodi, kommentaare ja analüüsi.
Notebook-i kood ei tohi testeri peal käivitamisel visata vigu ning peab defineerima täpselt samad muutujad ja funktsioonid, mida testid ootavad.
Testimine:

Testeri peal on lubatud järgmised teegid: numpy, pandas, seaborn, matplotlib, scikit-learn.

Mall:

import numpy as np
import pandas as pd
from collections import Counter

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import recall_score

# Ülesande eesmärk:
# Luua KNN mudel rinnavähi andmete klassifitseerimiseks.
# Hinnata mudeli võimet tuvastada pahaloomulisi kasvajaid.


# 1. Andmestiku laadimine
# load_breast_cancer() tagastab sõnastiku-laadse objekti, mis sisaldab:
# - data: tunnuste väärtused (n_samples, n_features)
# - target: sihtmuutuja (0 = malignant, 1 = benign)
# - feature_names: tunnuste nimed
# - target_names: klasside nimed
data = None

X = None
y = None
feature_names = None
target_names = None


# 2. Andmete kirjeldamine (DataFrame)
# Loo DataFrame tunnustest ja lisa veerg "diagnosis" tekstiliste klassidega ('malignant', 'benign')
df = None

# Siin võiks uurida DataFrame struktuuri:
# - mis tüüpi andmed on
# - kuidas väärtused on jaotunud
# - kas on puuduvaid väärtusi


# 3. Treening- ja testandmete jagamine
# Kasuta train_test_split, jaga andmestik 80/20 suhtega, kasuta stratify=y
X_train = None
X_test = None
y_train = None
y_test = None

# 4. Andmete skaleerimine (StandardScaler)
# Fit ainult treeningandmetel, transform mõlemad komplektid
scaler = None
X_train_scaled = None
X_test_scaled = None

# 5. KNN implementeerimine käsitsi
def my_knn_predict_single(X_train, y_train, x_new, k=5):
    """
    Ennusta ühe uue punkti klass KNN abil.
    Sammud:
    1) Arvuta eukleidiline kaugus x_new ja kõigi X_train punktide vahel
    2) Leia k lähimat treeningpunkti
    3) Võta nende punktide klassid
    4) Tee enamus-hääletus (Counter)
    (Enamus-hääletus tähendab, et valitakse see klass, mida lähimate naabrite seas esineb kõige rohkem.)
    """
    pass


def my_knn_predict(X_train, y_train, X_new, k=5):
    """
    Ennusta mitme punkti klassid, kutsudes my_knn_predict_single iga punkti jaoks
    """
    pass

# 6. Ennustamine ja hindamine
# Ennusta testandmestiku punktid, arvuta recall pahaloomulise (malignant) klassi jaoks
my_preds = None
score = None # malignant_recall score

# 7. Kokkuvõte
# Kirjuta lühike kokkuvõte:
# - miks skaleerimine KNN puhul oluline
# - k väärtuse mõju bias/variance
# - kuidas hinnata mudeli sobivust pahaloomuliste tuvastamiseks
summary = ""