import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def pierw(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1

eps1=1e-14
eps2=9e-16

d=0.001
a=-1
for b in np.arange(-10,10,d):
    if np.sign(pierw(a))!=np.sign(pierw(b)):
        prw=optimize.ridder(pierw,a,b,xtol=eps1,rtol=eps2,full_output=True)
        plt.plot(prw[0],0,'o')
        print("%4d   %19.16f" % (prw[1].iterations,prw[0]))
    a=b


x = np.arange(-10, 1, d)
plt.plot(x,pierw(x))
plt.axhline(y=0,color='k')
plt.grid()

plt.show()