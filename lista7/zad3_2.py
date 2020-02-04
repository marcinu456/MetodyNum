import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
## set initial conditions and parameters
g = 9.81            # acceleration due to gravity
th = 45.            # set launch angle
th = th * np.pi/180.   # convert launch angle to radians
v0 = 100.0           # set speed
k = 0.35             # controls strength of air drag

x0=0                # specify initial conditions
y0=0
vx0 = v0*np.sin(th)
vy0 = v0*np.cos(th)

## define function to compute f(X,t)
def f_func(state,time):
    f = np.zeros(4)    # create array to hold f vector
    f[0] = state[2] # f[0] = x component of velocity
    f[1] = state[3] # f[1] = x component of velocity
    f[2] = - k*(f[0]**2 + f[1]**2)**(0.5)*f[0]         # f[2] = acceleration in x direction
    f[3] = -g - k*(f[0]**2 + f[1]**2)**(0.5)*f[1]       # f[3] = acceleration in y direction
    return f

## set initial state vector and time array
X0 = [ x0, y0, vx0, vy0]        # set initial state of the system
t0 = 0.
# tf = input("Enter final time: ")
# tau = input("Enter time step: ")
tf = 3
tau = 0.05

# create time array starting at t0, ending at tf with a spacing tau
t = np.arange(t0,tf,tau)   

## solve ODE using odeint
X = odeint(f_func,X0,t) # returns an 2-dimensional array with the 
                        # first index specifying the time and the
                        # second index specifying the component of
                        # the state vector

# putting ':' as an index specifies all of the elements for
# that index so x, y, vx, and vy are arrays at times specified 
# in the time array
x = X[:,0]  
y = X[:,1] 
vx = X[:,2] 
vy = X[:,3]



plt.plot(x,y)

plt.show()