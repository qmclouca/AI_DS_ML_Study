import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 5, 11)
print (x)
y = x ** 2

plt.plot(x, y, 'b--')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g*-.')

plt.show()


