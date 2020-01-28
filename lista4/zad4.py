from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

circle = plt.Circle((0, 0), 2, color='b',fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)
x = np.arange(-3.0, 3, 0.00001)
y1 = (x+np.exp(-x))**(1/3)*(-1)
y2 = x-(2*x*x+np.tan(x))**(1/2)
y3 = (2*x*x+np.tan(x))**(1/2) + x
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)


przyb=3



def fdz(x):
    return [x[0]+np.exp(-1*x[0])+x[1]**3,
            x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0])]

odp=[]
xz=[np.array([-1.270,-1.260]),np.array([-0.720,-0.700]),np.array([1.200, 1.210])]
for i in xz:
    x1=optimize.root(fdz,i)
    if x1.success:
        x=round(x1.x[0],przyb)
        y=round(x1.x[1],przyb)
        if x**2+y**2<=4  :
            if  [round(x1.x[0],przyb),round(x1.x[1],przyb)] not  in odp:
                # print(round(x1.x[0],3),round(x1.x[1],3))
                odp.append([round(x1.x[0],przyb),round(x1.x[1],przyb)])
                ax.plot((round(x1.x[0],przyb)), (round(x1.x[1],przyb)), 'o', color='r',markersize=5)
#print(odp)
ax.axis('equal')
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))
print(odp)

plt.grid()
plt.show()