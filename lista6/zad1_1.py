import numpy as np 
from scipy.misc import derivative

def f(x):
    return np.log(np.tanh(x/(x**2+1)))


x = 0.2
h = 0.01
np1_5 = derivative(f, x, dx=h,n=1,order=5)
np2_5 = derivative(f, x, dx=h,n=2,order=5)
np3_5 = derivative(f, x, dx=h,n=3,order=5)

print(f"h={h}")
print(f"f'({x})={np1_5}")
print(f"f''({x})={np2_5}")
print(f"f'''({x})={np3_5}")

