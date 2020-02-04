import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
# punkt brzegowy a
a=4.6
n=1000 
# krok - stała sieci
h=2*a/n
#lambda
lam=0.2
# elementy diagonalne jest ich n-1
d=np.fromfunction(lambda i:1/h**2+0.5*(-a+(i+1)*h)**2+lam*(-a+(i+1)*h)**4 ,(n-1,),dtype=float)
# elementy nad/pod przekątną jest ich n-2
g= -0.5/h**2*np.ones(n-2)
# 
data=[d.tolist(),g.tolist(),g.tolist()]
positions=[0,1,-1]
# tworzenie macierzy rzadkiej za pomocą funkcji diags()
# wybieramy  format csc preferowany przez eigsh() z opcją sigma
Hm=diags(data,positions,(n-1,n-1)).tocsc()

#obliczymy 4 wartości własne k=4 leżace najbliżej sigma=0 
# użycie opcji sigma wymaga ustawienia which='LM'
#
eH,vH=eigsh(Hm,k=4,sigma=0.0,which='LM')

print('wartości własne\n')
print(eH)


xx=np.arange(h-a,a-h+1e-12,h)
for i in range(4):
    nv=1/np.sqrt((h*(vH[:,i]**2)).sum())  #normowanie
    plt.plot(xx, nv*vH[:,i])
    tyt='E='+str(round(eH[i],2))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(tyt)
    plt.show()