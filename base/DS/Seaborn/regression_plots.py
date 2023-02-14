# %%
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
tips.info()

sns.lmplot(x='total_bill', y='tip', data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'])
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'],scatter_kws={'s': 100})
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='sex', row='time')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='day', aspect=0.6, size=8)
# %%
