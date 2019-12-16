from scipy import optimize
import numpy as np

def fdz(x):
    return [np.tan(x[0])-x[1]-1,
            np.cos(x[0])-3*np.sin(x[1])]

odp=[]

for a in np.arange(0, 1.5, 0.01):
	for b in np.arange(0, 1.5, 0.01):
		x0 = np.array([a,b])
		x1 = optimize.root(fdz, x0)
		if x1.success:
			if(x1.x[0]>=0 and x1.x[0]<=1.5):
				x1.x[0] = round(x1.x[0], 7)
				if x1.x[0] not in odp:
					print(x1.x)
					odp.append(x1.x[0])
print(odp)