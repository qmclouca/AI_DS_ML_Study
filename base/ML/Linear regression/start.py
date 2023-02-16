#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# Conhecendo o dataset
USAhousing = pd.read_csv('/home/odolfo/AI/AI_DS_ML_Study/base/ML/Material de estudo/Regressões Lineares/USA_Housing.csv')
USAhousing.head()
USAhousing.info()
USAhousing.describe()
USAhousing.columns

#sns.pairplot(USAhousing)
#sns.heatmap(USAhousing.corr(), annot=True)

#Variáveis dependentes e independentes
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
         'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

X_test.shape[0]

lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)

coefs = pd.DataFrame(lm.coef_, X.columns, columns=['Coeficientes'])
coefs

predict = lm.predict(X_test)
predict

#plt.scatter(y_test, predict)
sns.distplot((y_test-predict), bins=50)

print('MAE', metrics.mean_absolute_error(y_test, predict))
print('MSE', metrics.mean_squared_error(y_test, predict))
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, predict)))
# %%
