import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
dx=np.array([0.2, 2, 20, 200, 2000, 20000],dtype=float)
dy=np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433],dtype=float)

#find y'(x) x =2.1
wl_2 = CubicSpline(dx, dy)
plt.plot(dx, dy,'o')
xw2 = np.arange(1.0, 20000, 0.01)
plt.plot(xw2, wl_2(xw2))
plt.grid()
plt.legend(['dane',  'wl_2'], loc='best')
plt.show()
pierw=wl_2.roots(0, 500)
print(5.50,wl_2(5.50))
print(500,wl_2(500))