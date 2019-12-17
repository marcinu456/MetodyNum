from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import time


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
    

def rzut(x,y,a,v,vy):
    for t in np.arange(0.0,100.0, 0.01):
        g=9.81
        x_p=v*np.cos(a)*t
        y_p=2+v*np.sin(a)*t-((g*t*t))/2
        if x_p<=10.0: #jeśli punkt x jest mniejszy niż 10 dodawaj do listy
            #print(y_p)
            x.append(x_p)
            y.append(y_p)
            vy.append(v*np.sin(a)-(g*t))
        else:
            break


def check(v,a,vy):
    vx=v*np.cos(a)
    #print(np.abs(vy[-1]/vx))

    #jeśli wysokość jest pomiedzy <2.95;3.05> i tangens <0.95;1.05> zwróć false
    if (2.95 <= y[-1] <= 3.05) and (0.95<=(np.abs(vy[-1]/vx))<=1.05) :#and (2.95 <= y[-1] <= 3.05):
        print(f"x={x[-1]},y={y[-1]}")
        print(f"vx={vx},vy={vy[-1]}")
        print(f"v poczakowe={v}, kat poczatkowy={np.rad2deg(a)}")
        print(f"v poczakowe={v}, kat poczatkowy radiany={(a)}")
        return False
    else:
        return True



if __name__ == '__main__':
    start_time = time.time()
    print("run")
    draw_line()
    #v=11.8
    
    ff=True
    for v in np.arange(10,11,0.1):
        for i in np.arange(10,90,0.1):
            if ff is True:
                a=np.deg2rad(i)
                x=[]#dlugość
                y=[]#wysokość
                vy=[]#prędkość y w danej chwili
                rzut(x,y,a,v,vy)
                ff=check(v,a,vy)

    
    print(len(x))
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.plot(x, y, linewidth=3)
    plt.grid()
    plt.show()