import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)
print(df.groupby('Company').mean())
print(df.groupby('Company').std())
print(df.groupby('Company').min())
print(df.groupby('Company').max())
print(df.groupby('Company').count())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])

group = df.groupby('Company')
print(group.sum()) # sum of all columns
print(group.describe()) # describe all columns

