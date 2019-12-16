import numpy as np
from scipy import linalg as lng

def get_hilbert(n):
    hilbert = np.zeros((n, n))
    for i in range(n):
        for k in range(n):
            hilbert[i][k] = 1 / (i + k + 1)
    return hilbert

N = (4, 8)
for n in N:
    print(f"\n\nn={n}")
    H = get_hilbert(n)
    Hodw = lng.inv(H)
    print("Maciez:")
    print(H)
    print('\nMaciez odwrotna:')
    print(Hodw)

print("\n\n\n")

for i in range(5, 21):

    print(f'{i} wyzn= {lng.det(get_hilbert(i))}')
