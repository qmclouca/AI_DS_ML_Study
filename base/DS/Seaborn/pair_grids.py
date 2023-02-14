# %%
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
iris.head(20)

iris['species'].value_counts()
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
g = sns.FacetGrid(data=tips, col='time', hue='sex', row='smoker')
g.map(sns.distplot, 'total_bill')
g.map(sns.distplot, 'tip')

# %%
