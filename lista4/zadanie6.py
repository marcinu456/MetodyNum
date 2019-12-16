from scipy import optimize
import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return [np.tan(x[0])-x[1]-1,np.cos(x[0])-3*np.sin(x[1])]

sol = []
xs = np.arange(0,1.5,0.01)
for a in np.arange(0,1.5,0.01):
    for b in np.arange(0,1.5,0.01):
        x0 = np.array([a,b])
        x1 = optimize.root(f,x0)
        if x1.success:
            if (x1.x[0]>=0 and x1.x[0]<1.5):
                x1.x[0] = round(x1.x[0],7)
                if x1.x[0] not in sol:
                    print(x1.x[0])
                    sol.append(x1.x[0])

y1 = np.tan(xs)-1
y2 = np.cos(xs)/3
plt.plot(xs,y1)
plt.plot(xs,np.sin(y2))
plt.show()