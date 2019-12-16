import numpy as np


def Gauss(A,B):#Gauss
    #Ilość kolumn
    n=len(A)

    #Pętla po kolumnach
    for k in range(n):
        i_max = abs(A[k:,k]).argmax() + k
        # Zamień wiersze
        if i_max != k:
            A[[k,i_max]] = A[[i_max, k]]
            B[[k,i_max]] = B[[i_max, k]]
        #Pętla po wierszu
        for row in range(k+1,n):
            f = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - f*A[k, k:]
            B[row] = B[row] - f*B[k]

    x = np.zeros(n)
    for k in range(n-1, -1,-1):
        x[k] = (B[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x

A=np.array([[0,0,2,1,2],
            [0,1,0,2,-1],
            [1,2,0,-2,0],
            [0,0,0,-1,1],
            [0,1,-1,1,-1]])
B =  np.array([[1],[1],[-4],[-2],[-1]])
print(Gauss(A,B))


x=np.array([[1.,0.,0.,0.,0.],
            [1.,1.,1.,1.,1.],
            [1.,3.,9.,27.,81.],
            [1.,5.,25.,125.,625.],
            [1.,6.,36.,216.,1296.]])
y=np.array([[-1.],[1.],[3.],[2.],[-2.]])
print(Gauss(x,y))