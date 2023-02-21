#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
#cancer.keys()
#print(cancer['DESCR'])

df_cancer = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df_cancer.head(10)
#sns.heatmap(df_cancer, yticklabels=False, cbar=False, cmap='viridis')
df_target = pd.DataFrame(cancer['target'], columns=['Cancer'])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df_cancer, np.ravel(df_target), test_size=0.30, random_state=101)

from sklearn.svm import SVC
model = SVC()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

param_grid = {'C': [0.1, 1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 'kernel': ['rbf']}
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)

grid.fit(x_train, y_train)
grid.best_params_
pred = grid.predict(x_test)

