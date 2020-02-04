import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t_0 = 0 
t_end = 10 
N = 1000
m = 5.5 # masa piłki, 
g = 9.81 # siła grawitacji
rho = 1.2 # gęstość powietrza
C_D = 0.35 # współczinnik oporu
d = 0.11 # średnia piłki, m
A = np.pi*d**2 # przekrój piłki
vp=100

t = np.linspace(t_0, t_end, N+1)

# time step
dt = t[1] - t[0]

# Create empty acceleration, velocity and position arrays
a = np.zeros((N+1,2))
v = np.zeros((N+1,2))
r = np.zeros((N+1,2))

# Set initial conditions
v[0] = (vp*np.cos(np.pi/6), vp*np.sin(np.pi/6)) # inital velocity, m/s
r[0] = (0,1)  # initial position, m



def F(r, v, t):
    return (0, -m*g) - 0.5*rho*C_D*A*abs(v)*v

# Solving equations of motion iteratively
for i in range(N):
    a[i] = F(r[i], v[i], t[i])/m
    print(a)
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + v[i]*dt

# Extract x and y coordinates
x = r[:,0]
y = r[:,1]


plt.plot(x,y)

# plt.show()