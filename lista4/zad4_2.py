from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

circle = plt.Circle((0, 0), 2, color='b',fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)

def fdz(x):
    return [x[0]+np.exp(-1*x[0])+x[1]**3,
            x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0])]

odp=[]
for i in np.arange(-2, 2,0.1 ):
    for j in np.arange(-2, 2, 0.1):
        x1=optimize.root(fdz,[j,i])
        if x1.success:
            if round(x1.x[0],2)**2+round(x1.x[1],2)**2<=4 :
                if  [round(x1.x[0],2),round(x1.x[1],2)] not  in odp:
                    print(round(x1.x[0],3),round(x1.x[1],3))
                    odp.append([round(x1.x[0],2),round(x1.x[1],2)])
                    ax.plot((round(x1.x[0],2)), (round(x1.x[1],2)), 'o', color='r',markersize=1)
#print(odp)
ax.axis('equal')
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))
plt.show()
