
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f_1(x, y): return ( x + np.exp(-x) + y**3 )
def f_2(x, y): return ( x**2 + 2*x*y - y**2 + np.tan(x) )

def f(x):
    return [f_1(x[0], x[1]), f_2(x[0], x[1])]

# only for plot
def f_1_r(x): return np.cbrt(-np.exp(-x) -x)
def f_2_r_1(x): return ( x - np.sqrt(2 * x**2 + np.tan(x)) )
def f_2_r_2(x): return ( x + np.sqrt(2 * x**2 + np.tan(x)) )
def f_o_p(x, r = 2): return np.sqrt( r**2 - x**2 )
def f_o_m(x, r = 2): return -np.sqrt( r**2 - x**2 )

if __name__ == "__main__":

    x0s = [
        np.array([-1.271, -1.269]),
        np.array([-0.714, -0.71]),
        np.array([1.2066, 1.2068]),
    ]

    index = 0
    for x0 in x0s:
        index += 1
        x1=optimize.root(f, x0)
        if x1.success:
            print(f'root {index}:\n\tx: {x1.x[0]} \n\ty: {x1.x[1]}')


    x = np.linspace(-2, 2, 1024000)

    plt.axis([-2, 2, -2, 2])

    # plot circle
    plt.plot(x, f_o_p(x), color='r')
    plt.plot(x, f_o_m(x), color='r')

    # plot functions
    plt.plot(x, f_1_r(x), color='b')
    plt.plot(x, f_2_r_1(x), color='g')
    plt.plot(x, f_2_r_2(x), color='g')

    plt.show()