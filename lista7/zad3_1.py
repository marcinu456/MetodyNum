import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint

def F(t, y, C_D,ra):
    print(y)
    return [y[1], -g - 0.5*C_D*A*ra*abs(y[1])*y[1]]
def grunt(t,y):
    return y[0]

t_0 = 0 
t_end = 20
g = 9.81 # siła grawitacji
rho = 1.2 # gęstość powietrza
C_D = 0.35 # współczinnik oporu
d = 0.11 # średnia piłki, m
A = np.pi*d**2 # przekrój piłki
kat = np.pi/6 # kąt w radianach
y_0 = 0.1
v_0 = 100
grunt.terminal = True

y40 = [y_0, v_0]




# Set initial conditions
#y40= [v_0*np.cos(kat), v_0*np.sin(kat)] # inital velocity, m/s
print(y40)

w4 = solve_ivp(lambda t,y:F(t,y,C_D,rho), [0,t_end], y40,events=grunt,atol=1e-12,rtol=1e-10)

print(w4.y[0,-1])

plt.plot(w4.t,w4.y[0],linewidth=3,color='blue')

plt.show()