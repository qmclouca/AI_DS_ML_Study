#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.distplot(train['Fare'], kde=False, color='green', bins=40)