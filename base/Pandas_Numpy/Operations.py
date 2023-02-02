import pandas as pd
import numpy as np
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head())

print(df['col2'].unique()) # returns an array of unique values
print(np.unique(df['col2'])) # returns an array of unique values

print(len(df['col2'].unique())) # returns an integer of the number of unique values
print(df['col2'].nunique()) # returns an integer of the number of unique values

print(df['col2'].value_counts()) # returns a series

print(df[(df['col1']>2) & (df['col2']==444)]) # returns a dataframe of the rows that meet the condition

def times2(x):
    return x*2

print(df['col1'].apply(times2)) # returns a series using pandas apply method to apply a function to a column

df['col1'].apply(lambda x: x*2) # returns a series using pandas apply method to apply a lambda function to a column

del df['col2'] # deletes a column

print(df.columns) # returns a list of the column names

print(df.index) # returns a list of the index names

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.sort_values(by='col2',inplace = True)) # returns a dataframe sorted by a column

print(df.isnull()) # returns a dataframe of boolean values indicating whether a value is null

print(df.dropna()) # returns a dataframe with null values dropped

df = pd.DataFrame({'col1': [1, 2, 3, np.nan], 'col2': [np.nan, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head())
print(df.fillna('FILL VALUE')) # returns a dataframe with null values filled

print(df['col1'].fillna(value=df['col1'].mean())) # returns a series with null values filled with the mean of the column

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}
df = pd.DataFrame(data)
print(df.head())
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C'])) # returns a dataframe with the values in column D pivoted