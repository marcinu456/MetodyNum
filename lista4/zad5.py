from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
r=4



ax.axis('equal')
def draw_line():

    #koszykarz
    x_k = [0, 0]
    y_k = [0, 2]
    plt.plot(x_k, y_k, linewidth=3)
    
    #kosz
    x_kosz = [9.5, 10.5]
    y_kosz = [3, 3]
    plt.plot(x_kosz, y_kosz, linewidth=3)
    

def rzut(x,y):
    for t in np.arange(0.0,2.0, 0.01):
        x_p=v*np.cos(a)*t
        y_p=2+v*np.sin(a)*t-((g*t*t))/2
        if x_p<=10.0:
            #print(y_p)
            x.append(x_p)
            y.append(y_p)


def check(x,y):
    if (44.0<=((y[-1]/x[-1])*(180/np.pi))<=46.0) and (2.95 <= y[-1] <= 3.05):
        print(f"x={x[-1]},y={y[-1]}")
        return False
    else:
        return True



if __name__ == '__main__':
    draw_line()
    #v=11.8
    g=9.81
    ff=True
    for v in np.arange(5,25,0.01):
        for i in np.arange(0,90):
            if ff is True:
                a=i*np.pi/180
                x=[]
                y=[]
                rzut(x,y)
                ff=check(x,y)
                #print(f"x={x[-1]},y={y[-1]}")

    
    print(len(x))

    plt.plot(x, y, linewidth=3)
    plt.grid()
    plt.show()