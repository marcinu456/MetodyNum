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


g=9.81 # stała g
def u2r(w): #układ dwóch równań
    #V0=w[0],alfa=w[1]
    tk=10/(w[0]*np.cos(w[1]))
    return[w[0]*np.sin(w[1])*tk-(g*tk**2/2)-1,w[0]*(np.sin(w[1])+np.cos(w[1]))-(g*tk)]


w0=[20.0,np.pi*50/180]

ws=optimize.root(u2r,w0)   
if ws.success:
    print("V0",ws.x[0])
    print("alfa",ws.x[1]*180/np.pi)

