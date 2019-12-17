
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return ( 2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1 )

def f_dx(x):
    return ( 2 * ( 4*x**3+ 36*x*2 + 61*x - 8 ) )

ab = [
    [-8.2, -8],
    [-4.2, -4],
    [0.121, 0.1220],
    [0.1220, 0.2]
]

roots = []
for a, b in ab:
    roots.append(optimize.ridder(f, a, b))

print('roots:')
index = 0
for r in roots:
    index += 1
    print(f'\tx_{index}: {r}')

x = np.linspace(-9, 2, 10000)
plt.plot(x,f(x))
plt.axhline(y=0,color='k')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()