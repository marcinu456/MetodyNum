from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


r=3

def fdz(x):
    #print(f'x={x[0]}, y={x[1]}')
    return [np.tan(x[0])-x[1]-1,
            np.cos(x[0])-(3*np.sin(x[1]))]

odp=[]
for i in np.arange(0, 3, 0.1 ):
    for j in np.arange(0, 3, 0.01):
        x1=optimize.root(fdz,[j,i])
        if x1.success:
            if 0 <=round(x1.x[0],r)<=1.5:# and round(x1.x[1],r)>=0 and round(x1.x[1],r)<=1.5 :
                if  [round(x1.x[0],r),round(x1.x[1],r)] not  in odp:
                    print(round(x1.x[0],r),round(x1.x[1],r))
                    odp.append([round(x1.x[0],r),round(x1.x[1],r)])
                    plt.plot((round(x1.x[0],r)), (round(x1.x[1],r)), 'o', color='r')


plt.axis('equal')
# plt.set_xlim((0, 3))
# plt.set_ylim((0, 3))
x = np.arange(0.0, 1.5, 0.001)
y = np.tan(x)-1
plt.plot(x, y)
z = np.cos(x)/3
for i in range(0, 5):
    plt.plot(x, np.sin(z)+(3.14*i))
plt.grid()
plt.show()
