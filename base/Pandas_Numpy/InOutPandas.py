import numpy as np
import pandas as pd

df = pd.read_csv('/home/odolfo/AI/AI_DS_ML_Study/base/Pasta2.csv',sep=',')
print(df)

df.to_csv("exemplo2.csv",sep=";",decimal=",")
df.to_excel("exemplo2.xlsx",sheet_name="Sheet1")
df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list')
print(df[0])