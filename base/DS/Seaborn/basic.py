#%%
import seaborn as sns

# Distribution plots

tips = sns.load_dataset('tips') # Load the tips dataset from the internet

tips.head() # Show the first 5 rows of the dataset  
# distplot
sns.rugplot(tips['total_bill']) # Rug plot of the total bill column
# kdeplot
sns.kdeplot(tips['total_bill']) # Rug plot of the total bill column
# pairplot
sns.distplot(tips['total_bill']) # Histogram of the total bill column
sns.distplot(tips['total_bill'], kde=False, bins=30) # Histogram of the total bill column

# joinplot

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg') # Scatter plot of total bill vs tip
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex') # Scatter plot of total bill vs tip
# rugplot



sns.pairplot(tips, hue='sex', palette='coolwarm') # Pair plot of the entire dataset

# %%
