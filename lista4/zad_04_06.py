
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f_1(x, y): return ( np.tan(x) - y - 1 )
def f_2(x, y): return ( np.cos(x) - 3*np.sin(y) )

def f(x): return [f_1(x[0], x[1]), f_2(x[0], x[1])]

# only fo plot
def f_1_p(x): return ( np.tan(x) - 1 )
def f_2_p_1(x, k=0): return ( 2*k*np.pi - np.arcsin(np.cos(x)/3/180*np.pi)*180/np.pi + np.pi )
def f_2_p_2(x, k=0): return ( 2*k*np.pi + np.arcsin(np.cos(x)/3/180*np.pi)*180/np.pi )

if __name__ == "__main__":

    x0s = [
        np.array([0.880, 0.882]),
        np.array([1.3290, 1.3296]),
        np.array([1.4345, 1.4355]),
        np.array([1.4748, 1.4749]),
        np.array([1.4970, 1.4975]),
    ]

    index = 0
    for x0 in x0s:
        index += 1
        x1=optimize.root(f, x0)
        if x1.success:
            print(f'root {index}:\n\tx: {x1.x[0]} \n\ty: {x1.x[1]}')
    
    x = np.linspace(-.05, 1.55, 1024)

    # plt.axis('equal')
    plt.axis([-1, 2.5, -5, 30])
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='r')
    plt.axvline(x=1.5, color='r')

    plt.plot(x, f_1_p(x), color='g')
    for i in range(-1, 7):
        plt.plot(x, f_2_p_1(x, k=i), color='b')
        plt.plot(x, f_2_p_2(x, k=i), color='b')

    plt.show()