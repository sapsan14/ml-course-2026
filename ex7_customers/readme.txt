Mall customers
Completion requirements
Mall Customersi klasterdamine
Kaubanduskeskuse turundustiim soovib eristada erinevaid külastajagruppe, et kavandada personaalseid pakkumisi ja planeerida üritusi. Sinu ülesanne on uurida lojaalsusprogrammi andmeid, rühmitada kliendid sarnastesse gruppidesse ning kirjeldada, mida iga grupp endast kujutab.

Eesmärk
Luua K‑meansi klasterdus, mis rühmitab kliendid aastase sissetuleku ja kulutusskoori põhjal ning annab äriliselt mõistetava ülevaate olulisematest segmentidest.

Andmestik
Fail mall_customers.csv asub ülesande kaustas ja sisaldab veerge CustomerID, Gender, Age, Annual Income (k$) ja Spending Score (1-100).
Andmestikus ei ole puuduvaid väärtusi ning see tuleb lahenduses säilitada.
Lingid
Andmestik: https://moodle.taltech.ee/pluginfile.php/1173148/mod_resource/content/1/mall_customers.csv
Notebooki mall: link
Ülesanded
1. Andmete laadimine ja esmane kontroll
Impordi vajalikud teegid (pandas, matplotlib, sklearn jne), loe CSV-faili DataFrame'i.
Veendu, et kohustuslikud veerud on olemas ja väärtused on loogilised (nt vanuste ja kulutuspunktide jaotused).
2. Tunnuste valik ja skaleerimine
Määra feature_columns list koos veergudega Annual Income (k$) ja Spending Score (1-100) ning loo X = df[feature_columns].
Kasuta StandardScalerit, et luua scaler ja X_scaled; skaleeritud andmetel peab olema nullkeskmine ja ühikhälve.
3. Küünarnuki meetod
Treeni KMeans-mudelid k = 1..10 (kasuta random_state=42 ja n_init=10).
Salvesta iga mudeli inertia_ väärtus järjendisse inertia_values ja väljasta (k, inertia) paarid, et hinnata murdepunkti.
4. Elbow graafik
Visualiseeri inertsuse muutus joondiagrammina, kus telgedel on k ja inertsus; lisa pealkiri, telje nimed ja võrgustik, et murdepunkt oleks selgelt loetav.
5. Lõplik mudel
Küünarnuki põhjal vali optimal_k = 5, treeni uus KMeans samade hüperparameetritega ning salvesta mudel muutujasse kmeans_model.
Salvesta cluster_labels ja cluster_centers ning lisa DataFrame'i täisarvuline veerg Cluster, mis sisaldab iga rea klastri ID-d.
6. Klientide visualiseerimine
Koosta hajuvusdiagramm, kus x-teljel on Annual Income (k$) ja y-teljel Spending Score (1-100), ning värvi punktid klastrite järgi. Lisa legend, teljemärgised ja pealkiri, mis kirjeldab, mida graafikust näha on.
7. Tsentroidid algses mõõtkavas
Teisenda cluster_centers tagasi algmõõtkavasse scaler.inverse_transform abil ja salvesta tulemus muutujasse cluster_centers_original_scale.
Kuva hajuvusdiagramm, kus algsed punktid ja tsentroidid on samal graafikul; kasuta tsentroidide jaoks selgelt eristuvat markerit, värvi ja annotatsiooni. e
8. Tekstiline kokkuvõte
Lisa Notebooki stringimuutuja summary, mis võtab 6–10 lausega kokku peamised klastrid, kirjeldab nende tüüpilisi sissetuleku/kulutuse tasemeid ja pakub ideid, kuidas turundus võiks iga segmenti kõnetada.
Esitamine
Esita lahendus Jupyter Notebookina nimega ex_mall_customers.ipynb, mis tugineb kaasa pandud mallile.
Notebook peab jooksma algusest lõpuni vigadeta ja sisaldama kõiki eelnevates punktides nõutud muutujaid, graafikuid ja kommentaare.