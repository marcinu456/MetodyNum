from scipy.linalg import hilbert
from scipy.linalg import eigh
import numpy as np

H = hilbert(6)
w1,v1 = eigh(H)
print("Wartości własne:",w1)
print("Wektory własne")
for v in v1:
    print(" > ",v)