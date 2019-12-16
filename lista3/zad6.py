import numpy as np
from scipy.linalg import hilbert


n=np.array([5,10,20])
print("n","    ","Norma","                 ","Wskaźnik uwarunkowania")
for i in range(0,3):
    H=hilbert(n[i])
    print(n[i],"    ",np.linalg.norm(H),"    ",np.linalg.cond(H))
