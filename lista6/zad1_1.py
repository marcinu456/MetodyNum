import numpy as np 
from scipy.misc import derivative

def f(x):
    return np.log(np.tanh(x/(x**2+1)))


x = 0.2

#f`(0.2)=4.50353
#f``(0.2)=-27.1412
#f```(0.2)=254.61

r=3


for h in np.arange(0,0.1,0.0001):
    np1_5 = derivative(f, x, dx=h,n=1,order=5)
    np2_5 = derivative(f, x, dx=h,n=2,order=5)
    np3_5 = derivative(f, x, dx=h,n=3,order=5)
    if 4.500 <=round(np1_5,r)<=4.510 and -27.145 <=round(np2_5,r)<=-27.140 and 254.600 <=round(np3_5,r)<=254.6102 :
        print(f"h={h}")
        print(f"f'({x})={np1_5}")
        print(f"f''({x})={np2_5}")
        print(f"f'''({x})={np3_5}")

