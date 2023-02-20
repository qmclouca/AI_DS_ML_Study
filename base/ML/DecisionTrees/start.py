#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('kyphosis.csv')
df.head(10)

sns.pairplot(df, hue='Kyphosis')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.drop('Kyphosis', axis=1), df['Kyphosis'], test_size=0.30)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)
predictions = dtree.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(x_train, y_train)
rfc_pred = rfc.predict(x_test)

print(confusion_matrix(y_test, rfc_pred))
print(classification_report(y_test, rfc_pred))
