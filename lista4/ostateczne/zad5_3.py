from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
#V0=? a=?
#x=0 y=2 pocztkowe

#Vx=V0*cos(a)
#Vy=V0*sin(a)-g*t

#x=V0*cos(a)*t
#y-V0*sin(a)*t-((g*t*t)/2)
#Vy=-Vx->V0+(sin(a)+cos(a))g*t=0

#obliczymy czas lotu piłki z rów(1)
#10=V0*cos(a)*t->tk=10/V0*cos(a)


#tk=10/V0*cos(a) pomocnicze
#V0*sin(a)*tk-(g*tk*tk/2)-1=0
#V0*(sin(a)+cos(a))-(g*tk)=0
fig, ax = plt.subplots()

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

g=9.81 # stała g
def u2r(w): #układ dwóch równań
    #V0=w[0],alfa=w[1]
    tk=10/(w[0]*np.cos(w[1]))
    return[w[0]*np.sin(w[1])*tk-(g*tk**2/2)-1,w[0]*(np.sin(w[1])+np.cos(w[1]))-(g*tk)]


w0=[10.4,np.pi*50/180]



def rzut(x,y,v,a):
    for t in np.arange(0.0,2.0, 0.01):
        x_p=v*np.cos(a)*t
        y_p=2+v*np.sin(a)*t-((g*t*t))/2
        if x_p<=10.0:
            x.append(x_p)
            y.append(y_p)


ws=optimize.root(u2r,w0)   
if ws.success:
    print("V0",ws.x[0])
    print("alfa",ws.x[1]*180/np.pi)
    V0=ws.x[0]
    a=ws.x[1]
    x=[]
    y=[]  
    rzut(x,y,V0,a)
    plt.plot(x, y, linewidth=3)
    draw_line()
    plt.grid()
    plt.show()

