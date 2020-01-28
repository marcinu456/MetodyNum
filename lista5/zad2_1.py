#zrobić lagrance
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
dx=np.array([1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3],dtype=float)
dy=np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334],dtype=float)

#find y'(x) x =2.1
wl_2 = CubicSpline(dx, dy)
print(wl_2(2.1,1))
plt.plot(dx, dy,'o')
xw2 = np.arange(1.0, 3, 0.01)
plt.plot(xw2, wl_2(xw2))
# plt.plot(2.1,wl_2(2.1,1),'ro')

mz_x = wl_2.roots()[1:-1]
mz_y = np.zeros(len(mz_x))
print('miejsce zerowe:', mz_x)
plt.plot(mz_x, mz_y, 'ob')
plt.grid()
plt.legend(['dane',  'wl_2'], loc='best')
plt.show()
