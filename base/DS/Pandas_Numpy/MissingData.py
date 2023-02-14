import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df) # print the DataFrame
print(df.dropna()) # drop rows with missing data
print(df.dropna(thresh=2)) # drop rows with missing data, but keep rows with at least 2 non-missing values
print(df.fillna(value='FILL VALUE')) # fill missing data with a value
print(df['A'].fillna(value=df['A'].mean())) # fill missing data with the mean of the column
print(df.fillna(method='ffill')) # fill missing data with the previous value