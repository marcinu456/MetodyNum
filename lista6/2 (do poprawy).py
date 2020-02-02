import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import CubicSpline
from scipy.misc import derivative


x = [0, 0.1, 0.2, 0.3, 0.4]
y = [0, 0.078348, 0.13891, 0.192916, 0.244981]


def bar(x):
    foo = np.polyfit(x,y,4)
    return foo[0]*x**4 + foo[1]*x**3 + foo[2]*x**2 + foo[3]*x +foo[4]

x0 = 0.2
dx = 0.00001
y0d = derivative(bar,x0,dx=dx)
print(y0d)

XX = np.linspace(0,0.5,50)
YY = []
for xx in XX:
    YY.append(bar(xx))
Y1 = []
for xx in XX:
    Y1.append(derivative(bar,xx,dx=dx))

plt.plot(XX,Y1, "+-y")
plt.plot(x0,y0d, "og")
plt.plot(XX,YY, "+-b")
plt.plot(x,y, "or")
plt.axis("equal")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f","","f'",""])
plt.show()