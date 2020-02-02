import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import simps 


def foo(x):
    return np.cos(2*np.arccos(x))

xmin = -1
xmax = 1

for w in [3,5,7,51]:
    XX = np.linspace(xmin,xmax,w)
    YY = []
    for xx in XX:
        YY.append(foo(xx))
    a = simps(YY,x=XX)
    print(a)

plt.plot(XX,YY)
plt.axis("equal")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()