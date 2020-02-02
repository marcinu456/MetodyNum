from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# y - lista o 2 składowych: y[0] = y, a y[1] = v  
# warunki początkowe  y0, vo
def f4(t,y,m,ra):
    return [y[1],-9.81 -ra/m*y[1]*np.abs(y[1])]
# initial condition
m=50.0
ro=10.1

y_0=0.1
v_0=10
t_max=10

y40 = [y_0, v_0]
t_ob4 = np.arange(0,t_max,1)

w4 = solve_ivp(lambda t,y:f4(t,y,m,ro), [0,t_max], y40)
print(w4.y[0,-1])

# Warunek  na osiągnięcie gruntu  przez spadające ciało
def grunt(t,y):
    return y[0]
# solve_ivp() oblicza pierwiastki równania grunt(t,y)=0

# Przerwanie obliczeń po kontakcie z gruntem
grunt.terminal = True

y_0=0.1
v_0=10
t_max=10
y40 = [y_0, v_0]
w4 = solve_ivp(lambda t,y:f4(t,y,m,ro), [0,t_max], y40,events=grunt,atol=1e-12,rtol=1e-10)
plt.rcParams.update({'font.size': 22})
fig,ax1=plt.subplots(figsize=(12, 6))
tyt='Rzut pionowy z odbiciami sprężystymi'
ax1.set_title(tyt)

ax1.plot(w4.t,w4.y[0],linewidth=3,color='blue')




ax1.set_xlabel('t')
ax1.set_ylabel("y")

plt.show()