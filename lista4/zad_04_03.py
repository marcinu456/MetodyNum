
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def predkosc_saturn(t):
    u = float(2510) #* m/s
    M_0 = float(2.8*10**6) #* kg
    m = float(13.3*10**3) #* kg/s
    g = float(9.81) #* m/s^2
    
    v = u * np.log(M_0/(M_0 - m*t)) - g*t

    return v-335


if __name__ == "__main__":
    t = np.linspace(0, 100, 100)

    a = 70
    b = 72
    t_335 = optimize.ridder(predkosc_saturn, a, b)
    print(f'Saturn osiągnie prędkość 335 m/s po {round(t_335, 4)} sekundach')


    plt.plot(t,predkosc_saturn(t))
    plt.axhline(y=0, color='k')
    plt.xlabel('t [s]')
    plt.ylabel('v \(-335 m/s\) [m/s]')

    plt.show()
