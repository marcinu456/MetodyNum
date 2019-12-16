import numpy as np
from scipy import optimize

x0=8 #liczba
x=x0
a=3 #pierwiastek

def f1(x,a):
    return (1/a)*((a-1)*x+(x0/(x**(a-1))))
for y in range(100):
    x=f1(x,a)
print(x)