from scipy.interpolate import lagrange
from scipy.misc import derivative
import numpy as np 

x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

wl = lagrange(x, y)

pwl=np.polyder(wl)
print(f"f'(0)= {pwl(0.2)}")
