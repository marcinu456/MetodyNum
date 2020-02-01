from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

# only for plot
def f_1_r(x): return np.cbrt(-np.exp(-x) -x)
def f_2_r_1(x): return ( x - np.sqrt(2 * x**2 + np.tan(x)) )
def f_2_r_2(x): return ( x + np.sqrt(2 * x**2 + np.tan(x)) )
def f_o_p(x, r = 2): return np.sqrt( r**2 - x**2 )
def f_o_m(x, r = 2): return -np.sqrt( r**2 - x**2 )


przyb=3


# funkcja dwóch zmiennych (x1=x[0],x2=x[1]) zwracająca dwie wartośći [f1,f2] 
def fdz(x):
    return [x[0]+np.exp(-1*x[0])+x[1]**3,
            x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0])]

odp=[]
#szukanie liczb znajdujących się w tym przedziale
xz=[np.array([-1.270,-1.260]),np.array([-0.720,-0.700]),np.array([1.200, 1.210])]
for i in xz:
    x1=optimize.root(fdz,i) #znajdź pierwiastek w funkcji
    if x1.success: #jeśli znalazł to
        x=round(x1.x[0],przyb)
        y=round(x1.x[1],przyb)
        if x**2+y**2<=4  : #jeśli znajdują się w kole i nie powtarzają się to dodaj do odp
            if  [round(x1.x[0],przyb),round(x1.x[1],przyb)] not  in odp:
                odp.append([round(x1.x[0],przyb),round(x1.x[1],przyb)])
                plt.plot((round(x1.x[0],przyb)), (round(x1.x[1],przyb)), 'o', color='r',markersize=5)


print(odp)


x = np.linspace(-2, 2, 1024000)
plt.axis([-2, 2, -2, 2])
# plot circle
plt.plot(x, f_o_p(x), color='r')
plt.plot(x, f_o_m(x), color='r')

# plot functions
plt.plot(x, f_1_r(x), color='b')
plt.plot(x, f_2_r_1(x), color='g')
plt.plot(x, f_2_r_2(x), color='g')

plt.grid()
plt.show()