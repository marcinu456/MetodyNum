import matplotlib.pyplot as plt 
import numpy as np
from scipy.special import roots_legendre


def  fzc(x):#całka
    return np.log(x)/(x**2-2*x+2)

a = 1
b = np.pi


w = [2,4] #węzły
for n in w:
    xi,ai = roots_legendre(n)
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i] * fzc((b+a)/2 + (b-a)/2*xi[i])
    print("%4d  %18.15f" %(n, I_n))
