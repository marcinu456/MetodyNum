import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
dx=np.array([0.2, 2, 20, 200, 2000, 20000])
dy=np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])


lgx=np.log(dx)
lgy=np.log(dy)
lgcs=CubicSpline(lgx, lgy)
# xw = [5,50,5000]
# d=np.exp(lgcs(np.log(xw)))

xw2 = np.arange((0.2), (20000), 1)
d2=np.exp(lgcs(np.log(xw2)))

plt.plot(dx,dy,'o')
plt.plot(xw2,d2)
plt.xscale('log')
plt.yscale('log')
plt.show()
