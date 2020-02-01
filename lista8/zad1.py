from scipy.linalg import eig
import numpy as np

W = np.array([[-1,-4,1],[-1,-2,-5],[5,4,3]])
w1,v1 = eig(W)
print("Wartości własne:",w1)
print("Wektory własne")
for v in v1:
    print(" ",v)