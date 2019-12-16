import numpy as np


def metod1(x):
    #return np.power(x**2-1, .5)-1
    return (np.sqrt(x**2+1)-1)

def metod2(x):
    return (x**2) / ( np.sqrt(x**2+1)+1 )
    #return np.power((1/np.power(2,i)),2)/(np.sqrt(np.power((1/np.power(2,i)),2)+1)+1)

for n in range(2, 27, 2):
    x = 2**(-n)
    m1 = metod1(x)
    m2 = metod2(x)
    r = m1 - m2
    print(f"\nn = {n}   x = {x}")
    print(f"Metoda 1: {m1}")
    print(f"Metoda 2: {m2}")
    print(f"różnica:  {r}")
