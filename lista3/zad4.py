import numpy as np
from scipy import linalg
x=np.array([[1,0,0,0,0],
            [1,1,1,1,1],
            [1,3,9,27,81],
            [1,5,25,125,625],
            [1,6,36,216,1296]])
y=np.array([[-1],[1],[3],[2],[-2]])
print(linalg.solve(x,y))