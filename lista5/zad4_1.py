import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
dx=np.array([0.2, 2, 20, 200, 2000, 20000],dtype=float)
dy=np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433],dtype=float)
wl_2 = lagrange(np.log10(dx), np.log10(dy))



plt.plot(np.log10(dx), np.log10(dy),'o')
xw2 = np.linspace(np.log10(0.2), np.log10(20000))
plt.plot((xw2), (wl_2(xw2)))
plt.legend(['dane',  'wl_2'], loc='best')
plt.show()





# lgx=np.log(dx)
# lgy=np.log(dy)
# lgcs=CubicSpline(lgx, lgy)
# # xw = [5,50,5000]
# # d=np.exp(lgcs(np.log(xw)))

# xw2 = np.arange((0.2), (20000), 1)
# d2=np.exp(lgcs(np.log(xw2)))

# plt.plot(dx,dy,'o')
# plt.plot(xw2,d2)
# plt.xscale('log')
# plt.yscale('log')
# plt.show()
