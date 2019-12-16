import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

u=2510
M0=2.8*(10**6)
m=13.3*(10**3)
g=9.81

def f(t):
    return u*np.log(M0/(M0-m*t))-g*t-335


print(optimize.newton(f,0))
t= np.arange(0,100,0.01)
plt.plot(optimize.newton(f,0),0,'o')
plt.plot(t,f(t))
plt.grid()
plt.show()