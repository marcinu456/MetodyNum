import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
def f1(t, y): 
    return np.sin(t*y)
y0=[2]
wyn = solve_ivp(f1, [0, 6], y0)
print('t=',wyn.t)
print('\ny=',wyn.y[0])


fig,ax1=plt.subplots(figsize=(12, 6))
ax1.plot(wyn.t,wyn.y[0],'o')
ax1.set_xlabel('t')
ax1.set_ylabel('y')
plt.show()