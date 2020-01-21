import matplotlib.pyplot as plt 
from scipy.interpolate import CubicSpline 
from scipy.interpolate import Akima1DInterpolator
import numpy as np



xt1 = [0.2,2,20,200,2000,20000]
yt1 = [103,13.9,2.72,0.8,0.401,0.433]

lgx = np.log(xt1)
lgy = np.log(yt1)
xw=[5,50,5000]
lgcs = Akima1DInterpolator(lgx,lgy) 
print(np.exp(lgcs(np.log(xw))))
#xx = np.linspace(np.log(0.2),np.log(20000),num=200)
gx = np.arange(0.2,20000,1)
gy = np.exp(lgcs(np.log(gx)))
plt.plot(xt1,yt1,'o')
plt.plot(gx,gy)
plt.xscale('log')
plt.yscale('log')
#plt.plot(xx,lgcs(xx))
plt.show()