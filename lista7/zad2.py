from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def f72(t,y,q,w,A):
    return [y[1],-y[1]/q-np.sin(y[0])+A*np.cos(w*t)]


l=0.5
g=9.81
y720=[0.01,0]
q=2
w0=np.sqrt(q/l)
w=2.0/3.0
A=0.5
tmax=300
t72=np.arange(0.0,tmax,0.03 )
wyn72=solve_ivp(lambda t,y:f72(t,y,q,w,A), [0,tmax], y720, t_eval=t72)
#plt.plot(t72/w0,wyn72.y[0])
plt.plot(wyn72.y[1],wyn72.y[0])
plt.show()
