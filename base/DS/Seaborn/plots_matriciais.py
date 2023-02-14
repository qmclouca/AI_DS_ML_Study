# %%
import seaborn as sns
fights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

fights.head()
tips.head()
crr = tips.corr()
sns.heatmap(crr, annot=True, cmap='coolwarm')

pf = fights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(pf, cmap='magma', linecolor='white', linewidths=1)
sns.clustermap(pf, cmap='coolwarm', standard_scale=1)
# %%

