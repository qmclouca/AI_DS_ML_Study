import numpy as np
import pandas as pd

# Series
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. The basic method to create a Series is to call:

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

serie1 = pd.Series(data=my_list, index=labels)
print(serie1)

serie2 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
serie3 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

print(serie2 + serie3);
