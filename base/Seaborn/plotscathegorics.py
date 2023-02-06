# %%
import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')

# barplot
#sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# countplot
#sns.countplot(x='sex', data=tips)

# boxplot
#sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
#sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker', palette='rainbow')
#sns.boxplot(x='day', y='total_bill', data=tips, palette='rainbow', hue='sex')
#sns.boxplot(data=tips, orient='h', palette='rainbow')

# violinplot
# sns.violinplot(x='day', y='tip', data=tips, hue='sex', split=True)

# stripplot
# sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')

# swarmplot
# sns.swarmplot(x='day', y='total_bill', palette='rainbow', data=tips, hue='sex')

#Swarmplot and violinplot
# sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
# sns.violinplot(x='day', y='total_bill', data=tips, palette='rainbow')

#catplot
sns.catplot(x='sex', y='total_bill', data=tips, kind='bar') # kind can be bar, count, box, violin, strip, swarm, point, bar, or boxen

tips.head()

# %%
