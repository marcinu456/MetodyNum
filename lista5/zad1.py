import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
dx=np.array([0,3,6],dtype=float)
dy=np.array([1.225,0.905,0.652],dtype=float)
wl_2 = lagrange(dx, dy)
print(wl_2)
plt.plot(dx, dy,'o')
xw2 = np.arange(0.0, 6.5, 0.01)
plt.plot(xw2, wl_2(xw2))
plt.legend(['dane',  'wl_2'], loc='best')
plt.show()