import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 1.5, 0.00001)
y = np.cos(x) - 3 *np.sin((np.tan(x)-1))

fig, ax = plt.subplots()
plt.plot(x, y)
plt.grid()
ax.axhline(y=0, color='k')

plt.show()