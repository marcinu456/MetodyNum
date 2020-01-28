import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange


dx=np.array([0.2, 2, 20, 200, 2000, 20000],dtype=float)
dy=np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433],dtype=float)
wl_2 = lagrange(np.log(dx), np.log(dy))

plt.plot((dx), (dy),'o')
# xw2 = np.linspace(np.log10(0.2), np.log10(20000))
xw2 = np.arange((0.2), (20000), 1)
plt.plot((xw2), np.exp(wl_2(np.log(xw2))))
plt.legend(['dane',  'wl_2'], loc='best')
plt.xscale('log')
plt.yscale('log')
plt.show()

