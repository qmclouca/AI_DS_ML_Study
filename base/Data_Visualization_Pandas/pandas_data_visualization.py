#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('seaborn') # ggplot, fivethirtyeight, bmh, dark_background, seaborn

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

#df1['A'].hist(bins=20)
#df2.plot.area(alpha=0.4)

#df2.plot.bar(stacked=True)
#df1['A'].plot.hist(bins=50)

#df1['A'].plot.line(x=df1.index, y='B', figsize=(12, 3), lw=1)

#df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
#df1.plot.scatter(x='A', y='B', s=df1['C']*50, cmap='coolwarm')
df2.plot.box()
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')

# %%
