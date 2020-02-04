import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import lagrange
from scipy.misc import derivative


x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])
wl = lagrange(x, y)




pwl=np.polyder(wl)
print(f"f'(0)= {pwl(0)}")
pwll=np.polyder(pwl)
print(f"f''(0)= {pwll(0)}")
