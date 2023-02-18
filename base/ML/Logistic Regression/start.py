#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

train = pd.read_csv('/home/odolfo/AI/AI_DS_ML_Study/base/ML/Material de estudo/Regressão Logística/titanic_train.csv')
train.head()

train.info()

#sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
sns.set_style('whitegrid')

#sns.countplot(x='Survived', data=train, hue='Sex', palette='RdBu_r')

#sns.countplot(x='Survived', data=train, hue='Pclass', palette='rainbow')

#sns.distplot(train['Age'].dropna(), kde=False, color='darkred', bins=30)

#sns.countplot(x='SibSp', data=train)

#train[train['SibSp'] == 0]['Age'].hist(bins=30)

#sns.distplot(train['Fare'], kde=False, color='green', bins=40)

#plt.figure(figsize=(12, 7))
#sns.boxplot(x='Pclass', y='Age', data=train, palette='winter')
# cleaning data
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)
del train['Cabin']
train.dropna(inplace=True)
#convert categorical features
sex = pd.get_dummies(train['Sex'], drop_first=True)
embark = pd.get_dummies(train['Embarked'], drop_first=True)
train.drop(['Sex', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
train = pd.concat([train,sex,embark], axis=1)
del train['Embarked']
train.head(50)

#SETUP TRAINING AND TESTING DATA
x_train, x_test, y_train, y_test = train_test_split(train.drop('Survived', axis=1), train['Survived'], test_size=0.30, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)

predictions = logmodel.predict(x_test)

print(classification_report(y_test, predictions))

print(confusion_matrix(y_test, predictions))
# %%
