import pandas as pd
import numpy as np

# Read the file
df = pd.read_csv('/home/odolfo/AI/AI_DS_ML_Study/DB/SF_Salaries/Salaries.csv',sep=',')
print(df.head())
print(df.info())
df_BaseSalary = df[df['BasePay'].str.contains('Not Provided')==False]
print("base salary:")
print(df_BaseSalary.info())
df_BaseSalary = pd.to_numeric(df_BaseSalary['BasePay'], downcast='float')
