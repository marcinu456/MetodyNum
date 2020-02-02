import numpy as np
from scipy.special import roots_legendre
def  fzc(x):
    return ((np.cos(x)-np.exp(x)) / (np.sin(x)))

a = -1
b = 1

for n in np.arange(1,11):
    xi,ai = roots_legendre(n)
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i] * fzc((b+a)/2 + (b-a)/2*xi[i])
    print("%4d  %18.10f" %(n, I_n))