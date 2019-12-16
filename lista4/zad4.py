from scipy import optimize
import numpy as np

def fdz(x):
    return [x[0]+np.exp(-x[0])+x[1]**3,
            x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0])]

odp=[]
for i in np.arange(-2, 2,0.1 ):
    for j in np.arange(-2, 2, 0.1):
        x1=optimize.root(fdz,[j,i])
        if x1.success :
            if  [round(x1.x[0],2),round(x1.x[1],2)] not  in odp:
                #print(x1.x)
                odp.append([round(x1.x[0],2),round(x1.x[1],2)])
print(odp)

