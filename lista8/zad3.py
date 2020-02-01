from scipy.sparse.linalg import eigsh
import numpy as np


n10a=[]
n10b=[]
n100a=[]
n100b=[]

N= [10,100]
for n in N:

    diag_s1=-1*np.ones(int(n)-1)
    diag=2*np.ones(int(n))   
    H = np.diag(diag) + np.diag(diag_s1, k=1) + np.diag(diag_s1, k=-1)
    eH,vH = eigsh(H,k=3, which="SM")
    for i in range(0,3):
        if n==10:
            n10a.append(eH[i])
            n10b.append(vH[:, i])
        else:
            n100a.append(eH[i])
            n100b.append(vH[:, i])


print("dla n = 10")
print(n10a)
print(n10b)
    
print("dla n = 100")
print(n100a)
print(n100b)


