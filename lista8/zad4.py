import numpy as np 
from scipy.integrate import solve_ivp
from scipy import optimize
import matplotlib.pyplot as plt

y_0 = 0
t_k = np.pi
y_k = 0

def fzb4(t,y):
    return [y[1], -np.sin(y[0])-1]

def f2b1(a):
    y0 = [y_0, a]
    woh = solve_ivp(fzb4, [0,t_k],y0,atol=1e-10,rtol=1e-8)
    return woh.y[0,-1]-y_k

a0 = 1
#eps1 = 1e-12
a = optimize.ridder(f2b1,2.69,2.90,rtol=1e-10, maxiter=200)
print(a,' ',f2b1(a))
y0 = [y_0,a]
woh = solve_ivp(fzb4,[0,t_k],y0,atol=1e-10,rtol=1e-8)
plt.plot(woh.t,woh.y[0])
plt.scatter(np.pi,0,color='red')
plt.xlabel('t')
plt.ylabel('dy')
plt.show()