
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#* https://www.wolframalpha.com/input/?i=x%5E4+%2B+%285%2Bi%29x%5E3+-+%288-5i%29x%5E2+%2B+%2830-14i%29x+-+84

def w(x):
    z = x**4 + (5 + 1j)*x**3 - (8 - 5j)*x**2 + (30 - 14j)*x - 84
    return [z.real, z.imag]

def w_r(x): return w(x)[0]
def w_i(x): return w(x)[1]

if __name__ == "__main__":

    ab_r = [
        [-7.25, -6.75],
        [1.5, 2.5],
    ]
    ab_i = [
        [-7.25, -6.75],
        [-0.5, 0.5],
        [1.5, 2.5],
    ]
    roots_r = []
    roots_i = []
    for a, b in ab_r:
        roots_r.append(optimize.ridder(w_r, a, b))
    for a, b in ab_i:
        roots_i.append(optimize.ridder(w_i, a, b))
    
    print('Real roots:')
    index = 0
    for r in roots_r:
        index += 1
        print(f'\tx_{index}: {r}')

    print('Complex roots:')
    index = 0
    for i in roots_i:
        index += 1
        print(f'\tx_{index}: {i} i')



    #* plot
    plt.axis([-11, 11, -500, 500])
    plt.axhline(y=0, color='k')

    x = np.linspace(-10, 10, 100000)
    plt.plot(x, w_r(x), color='b')
    plt.plot(x, w_i(x), color='r')

    plt.show()