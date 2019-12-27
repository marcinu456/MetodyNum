import numpy as np 
import matplotlib.pyplot as plt
import scipy
#from scipy.interpolate import CubicSpline 
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

re = [0.2,2,20,200,2000,20000]
cd = [103,13.9,2.72,0.8,0.401,0.433]
w1 = lagrange(np.log10(re),np.log10(cd))
#fk2 = interp1d(np.log10(re),np.log10(cd),kind="cubic")
#xs = np.linspace(np.log10(0.2),np.log10(20000),num=100)
#plt.plot(np.log10(re),np.log10(cd),'o')
xs = np.linspace(np.log10(0.2),np.log10(20000),num=100)
plt.plot(np.log10(re),np.log10(cd),'o')
plt.plot(xs,w1(xs))
#plt.plot(xs,cs(xs))
#plt.plot(xs,fk2(xs))
#plt.yscale("log")
#plt.xscale("log")
plt.show()