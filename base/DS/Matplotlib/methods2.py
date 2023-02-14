#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
fig, ax = plt.subplots(figsize=(9,10))
ax.plot(x, x**4,'b--', linewidth=6, alpha=0.5, label='X^4')
ax.plot(x, x**3,'#FF006673', linewidth=6, alpha=0.5, label='X^3', linestyle='--')
ax.plot(x, x**2,'g--')
ax.plot(x, x**1,'y--')
ax.set_xlim([0, 5])
fig.show()
# %%
