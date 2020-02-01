from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def tor(x,alpha,g,vp):
    return x*np.tan(alpha)-((g*x*x)/(2*vp*vp*np.cos(alpha)*np.cos(alpha)))

vp=10
alpha=45
g=9.81
x_m=(2*vp*vp*np.cos(alpha)*np.cos(alpha))/g
x= np.arange(0,x_m)

print("test")
plt.plot(x,tor(x,alpha,g,vp))
plt.show()