# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
x = np.linspace(0, 5, 11)

y = x ** 2

fig = plt.figure()	
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'r')
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Title')
axes2.plot(y, x, 'g')


fig, ax = plt.subplots()
ax.plot(x, x**3,'b--')
ax.plot(x, x**2,'r--')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')

fig, ax = plt.subplots(nrows=1, ncols=2)
for axe in ax:
    axe.plot(x, y, 'b')
    axe.set_xlabel('X')
    axe.set_ylabel('Y')
    axe.set_title('Title')

ax[0].plot(x, y, 'r')
ax[0].set_title('Title 1')
ax[1].plot(y, x, 'g')
ax[1].set_title('Title 2')
fig.show()

fig,ax = plt.subplots(nrows=3, ncols=3)
plt.tight_layout()
fig.show()

fig = plt.figure(figsize=(8,4), dpi=100)
fig, axes = plt.subplots(figsize=(12,3))
axes.plot(x, y, 'r', label='X Squared')
axes.plot(y, x, 'g', label='X Cubed')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')
fig.show()

axes.legend(loc=0)

fig.savefig('my_picture.png', dpi=200)

# %%
