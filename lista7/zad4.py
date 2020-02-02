from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

y_0=0
t_k=np.pi
y_k=0
def fzb4(t,y):
    return [y[1],-np.sin(y[0])-1]
def f2b1(a):
    y0=[y_0,a]
    woh=solve_ivp(fzb4,[0,t_k],y0,atol=1e-10,rtol=1e-8)
    return woh.y[0,-1]-y_k

a0=1
eps1=1e-12
a=optimize.newton(f2b1,a0,tol=eps1,maxiter=150)
print(a,' ',f2b1(a))
y0=[y_0,a]
woh=solve_ivp(fzb4,[0,t_k],y0,atol=1e-10,rtol=1e-8)
plt.plot(woh.t,woh.y[0])
plt.show()