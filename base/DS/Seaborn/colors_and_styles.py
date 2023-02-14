#%%
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.set_style('whitegrid') # white, darkgrid, whitegrid, dark, ticks
plt.figure(figsize=(12, 5))
sns.countplot(x='sex', data=tips)
sns.despine(left=True) # after defined remove the top and right spines from plot(s)
sns.lmplot(x='total_bill', y='tip', data=tips, aspect=1.5)

sns.set_context('poster', font_scale=1.2)
sns.lmplot(x='total_bill', y='tip', data=tips) # paper, notebook, talk, poster
# %%
