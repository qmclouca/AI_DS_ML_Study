import pandas as pd
import numpy as np

# Read the file
df = pd.read_csv('/home/odolfo/AI/AI_DS_ML_Study/DB/SF_Salaries/Salaries.csv',sep=',')
print(df.head())
print(df.info())

data = df[df['EmployeeName'] != 'Not Provided']
data = data[data['BasePay'] != 'Not Provided']
data = data[data['JobTitle'] != 'Not Provided']

data.reset_index(inplace=True, drop=True)

data['BasePay'] = data['BasePay'].astype(float)
data['OvertimePay'] = data['OvertimePay'].astype(float)
data['OtherPay'] = data['OtherPay'].astype(float)
data = data.drop(['Id', 'Notes', 'Agency', 'Status'], axis=1)

print(data.dtypes)
print(data.shape)

print(f"DataFrame has {data.shape[0]} rows and {data.shape[1]} columns")

print(f"Base Salary mean is: {data['BasePay'].mean()}")
print(f"Base Salary median is: {data['BasePay'].median()}")
print(f"Base Salary standard deviation is: {data['BasePay'].std()}")
print(f"Base Salary variance is: {data['BasePay'].var()}")
print(f"Base Salary max is: {data['BasePay'].max()}")
print(f"Base Salary min is: {data['BasePay'].min()}")

print(f"Overtime Salary mean is: {data['OvertimePay'].mean()}")
print(f"Overtime Salary median is: {data['OvertimePay'].median()}")
print(f"Overtime Salary standard deviation is: {data['OvertimePay'].std()}")
print(f"Overtime Salary variance is: {data['OvertimePay'].var()}")
print(f"Overtime Salary max is: {data['OvertimePay'].max()}")
print(f"Overtime Salary min is: {data['OvertimePay'].min()}")

print(data[data['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle'])
print(data[data['EmployeeName'] =='JOSEPH DRISCOLL']['TotalPayBenefits'])

print(data[data['TotalPayBenefits'] == data['TotalPayBenefits'].max()]['EmployeeName'])


print(data.describe().T)



