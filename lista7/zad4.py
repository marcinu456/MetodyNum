from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


y_0=0
t_k=np.pi
y_k=0
def fzb4(t,y):
    return [y[1],-np.sin(y[0])-1]
def f2b1(a):
    y0=[y_0,a]
    woh=solve_ivp(fzb4,[0,t_k],y0,atol=1e-10,rtol=1e-8)
    return woh.y[0,-1]-y_k
