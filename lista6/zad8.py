import numpy as np
from scipy.integrate import dblquad

# pierwszy argument dla całkowania wewnetrznego
def fxy(x, y): 
    return np.sin(np.pi*x)*np.sin(np.pi*(y-x))

# deklarujemy funkcję zwracającą dolną granicę calki wewnętrznej
def gfxy(x):
    return 0

# deklarujemy funkcję zwracającą górną granicę calki wewnętrznej
def hfxy(x):
    return x


wdxy=dblquad(fxy,0,1,gfxy,hfxy)
print(" %18.14f" %(wdxy[0]))