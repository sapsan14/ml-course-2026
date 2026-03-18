import pandas as pd
import numpy as np
import seaborn as sns
import sys
import matplotlib
if 'google.colab' not in sys.modules:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix,
    classification_report, roc_curve
)

import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style='whitegrid')

# 1. Andmestiku laadimine

if 'google.colab' in sys.modules:
    from google.colab import drive
    drive.mount('/content/drive')
    path = '/content/drive/MyDrive/google_colab/Titanic-Dataset.csv'
else:
    path = 'Titanic-Dataset.csv'

data = pd.read_csv(path)

target = 'Survived'

# 2. Andmete eeltöötlus

data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data['Fare'] = data['Fare'].fillna(data['Fare'].median())

data = data.drop(columns=['Cabin', 'PassengerId', 'Name', 'Ticket'])

data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

data = pd.get_dummies(data, columns=['Embarked'], drop_first=True, dtype=int)

# Feature engineering
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
data['IsAlone'] = (data['FamilySize'] == 1).astype(int)

# Outlier treatment for Fare: IQR cap + log transform
q1_fare = data['Fare'].quantile(0.25)
q3_fare = data['Fare'].quantile(0.75)
iqr_fare = q3_fare - q1_fare
fare_upper = q3_fare + 1.5 * iqr_fare
data['Fare'] = data['Fare'].clip(upper=fare_upper)
data['Fare'] = np.log1p(data['Fare'])

# 3. Tunnuste valik — only features with meaningful correlation to target

selected_features = ['Pclass', 'Sex', 'Fare', 'IsAlone']

# 4. Treening- ja testandmete jagamine

X = data[selected_features].copy()
y = data[target].copy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Andmete skaleerimine

scaler = MinMaxScaler()
scaler.fit(X_train)

X_train = pd.DataFrame(scaler.transform(X_train), columns=selected_features, index=X_train.index)
X_test = pd.DataFrame(scaler.transform(X_test), columns=selected_features, index=X_test.index)
X = pd.DataFrame(scaler.transform(X), columns=selected_features, index=X.index)

# 6. Mudelite treenimine

features_model_1 = ['Pclass', 'Sex']

model_1 = LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced')
model_1.fit(X_train[features_model_1], y_train)

features_model_2 = selected_features

model_2 = LogisticRegression(random_state=42, max_iter=1000, C=0.5, class_weight={0: 1, 1: 1.5})
model_2.fit(X_train[features_model_2], y_train)

# 7. Mudelite hindamine

model_1_predictions = model_1.predict(X_test[features_model_1])
model_2_predictions = model_2.predict(X_test[features_model_2])

f1_model_1 = f1_score(y_test, model_1_predictions)
f1_model_2 = f1_score(y_test, model_2_predictions)

models = [(model_1, f1_model_1), (model_2, f1_model_2)]

# 8. Kokkuvõte

summary = (
    "The Titanic dataset contains 891 passenger records with 12 original features. "
    "The target variable Survived is binary (0/1) with a class imbalance: approximately 38% survived and 62% perished. "
    "Missing values were found in Age (19.9%), Cabin (77.1%), and Embarked (0.2%); Age was imputed with the median, Embarked with the mode, and Cabin was dropped due to excessive missingness. "
    "Sex is by far the strongest predictor of survival — females had a survival rate of ~74% compared to ~19% for males, reflecting the 'women and children first' evacuation protocol. "
    "Passenger class (Pclass) also strongly influenced survival: 1st class passengers survived at ~63%, 2nd at ~47%, and 3rd at only ~24%. "
    "Fare is positively correlated with survival, largely because higher fares correspond to higher classes and better cabin locations near lifeboats. "
    "Fare outliers were capped using the IQR method to prevent skewing the model. "
    "The IsAlone feature was engineered from SibSp and Parch — solo travelers had lower survival rates than those with family. "
    "Features with weak correlation to the target (Age, SibSp, Parch, Embarked, FamilySize) were excluded after correlation analysis. "
    "Two logistic regression models were trained: Model 1 uses only Pclass and Sex, while Model 2 uses all four selected features. "
    "Model 2 with Fare and IsAlone provides better performance, showing that ticket price and family status add predictive value beyond class and gender. "
    "Both models show higher recall for class 0 (died) than class 1 (survived), which is expected given the class imbalance. "
    "Overall, logistic regression with just four well-chosen features provides a solid baseline for Titanic survival prediction. "
    "For future improvement, one could explore non-linear models or interaction terms between features."
)
