import numpy as np

def I(n):
    if n <= 1:
        return 1
    else:
        return np.exp(1) - (n * I(n-1))


for n in range(z, 21):
    print(f"n = {n}\tcałka: {I(n)}")