from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def foo(t,y):
    return np.sin(t*y)

y = [2, 2.5, 3, 3.5]
t_borders = [0,6]

for y0 in y:
    ans = solve_ivp(foo,t_borders,[y0])
    print("y0 =",y0)
    print("t =",ans.t)
    print("y =",ans.y[0])
    print()
    plt.plot(ans.t, ans.y[0], '+-')

plt.legend(['y0 = 2', 'y0 = 2.5', 'y0 = 3', 'y0 = 3.5'])
plt.show()