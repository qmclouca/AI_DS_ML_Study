# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# using object oriented method

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Title')
axes2.plot(y, x)
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
axes2.set_title('Title')

# %%
