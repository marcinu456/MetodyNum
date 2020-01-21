import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
dx=np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150],dtype=float)
dy=np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741],dtype=float)


def funq(x,a,b,c):
    return a*x*x+b*x+c

parm1,pcov=curve_fit(funq,dx,dy)
print(parm1)

plt.plot(dx, dy,'o')
xx=np.linspace(0, 11, num=100, endpoint=True)
plt.plot(xx, funq(xx,*parm1))
print("P na wysokości h=10.5km = ", funq(10.5,*parm1))
plt.show()