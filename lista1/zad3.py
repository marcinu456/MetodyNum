import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as lng


A = np.mat("[4 -2 1; -2 4 -2; 1 -2 4]")

B = np.mat("[4 2 0; 2 5 2; 0 2 4]")

w = np.mat("[1; -2; 3]")

AB = A.dot(B.T)
Aw = np.dot(A, w)
BAw = np.dot(B, Aw)
Aodw = lng.inv(A)
Bodw = lng.inv(B)

print("A * B =\n", AB)
print("A * w =\n", Aw)
print("B(A * w) =\n", BAw)
print("A^-1 =\n", Aodw)
print("B^-1 =\n", Bodw)
print("A wyz =", np.linalg.det(A))
print("B wyz =", np.linalg.det(B))