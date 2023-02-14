#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf

from plotly import __version__
print(__version__)

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
df.head()
df2 = pd.DataFrame({'Category':['A', 'B', 'C'], 'Values':[32, 43, 50]}) 
df2.head()
df.iplot(kind='scatter', x='A', y='B', mode='markers', size=5)

df2.iplot(kind='bar', x='Category', y='Values')
df.count().iplot(kind='bar')

df.iplot(kind='box')

df3 = pd.DataFrame({'x':[1,2,3,4,5,6,5,4,3,2,1], 'y':[10,20,30,20,10,40,32,43,54,65,43], 'z':[5,4,3,2,1,4,5,6,7,8,9]})

df3.iplot(kind='surface', colorscale='rdylbu')

df[['A', 'B']].iplot(kind='spread')

df.iplot(kind='bubble', x='A', y='B', size='C')

df['A'].iplot(kind='hist', bins=75)

df.scatter_matrix()

# %%
