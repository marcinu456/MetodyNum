import numpy as np
import matplotlib.pyplot as plt

x0=1.5 #liczba
x=x0
xl=[]
xl.append(x0)
a=2 #pierwiastek

def f1(x,a):
    return (1/a)*((a-1)*x+(x0/(x**(a-1))))
for y in range(30):
    x=f1(x,a)
    xl.append(f1(x,a))
print(x)
y=range(0,31)
plt.axhline(y=xl[-1],color='k')
plt.plot(y,xl)
#plt.show()



def niut(x0,a):
    x=[]
    for y in range(30):
        x0=(1/2)*(x0+(a/x0))
        print(x0)
        x.append(x0)
    return x

d=niut(x0,a)
print(d[-1])