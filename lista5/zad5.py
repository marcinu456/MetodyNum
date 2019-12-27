import numpy as np
import scipy 
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt

x = [1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7]
y = [6.008,15.722,27.13,33.772,5.257,9.549,11.098,28.828]

plt.plot(x,y,'o')
tp1 = np.polyfit(x,y,1)
tw1 = np.poly1d(tp1)
tp2 = np.polyfit(x,y,2)
tw2 = np.poly1d(tp2)
fxd = np.arange(1.0,4.0,0.01)
plt.plot(fxd,tw1(fxd))
plt.plot(fxd,tw2(fxd))
plt.show()

#funkcja kwadratowa
