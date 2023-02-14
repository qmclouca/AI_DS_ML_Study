import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside)) # zip is a built-in function
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index) # MultiIndex is a special type of index
print(hier_index)
df = pd.DataFrame(np.random.randn(6, 2), hier_index, columns=['A', 'B']) # 6 rows, 2 columns
print(df)
print(df.loc['G1'].loc[1].loc['A'])
df.index.names = ['Groups', 'Num']
print(df)
print(df.xs('G2')) # xs is cross section