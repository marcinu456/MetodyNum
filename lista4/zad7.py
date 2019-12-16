import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# wiel=[1,5+1j,-(8-5j),30-14j,-84]

# zw=np.roots(wiel)
# print(zw)
# print("")
# # for i in range(len(zw)):
# #     print((np.polyval(wiel,zw[i])))

# y=[]
# for i in range(len(zw)):
#     y.append(zw[i].real)
# print(len(zw))
# x = np.linspace(-4.7, 4.7, 4)
# plt.plot(x, y)
# plt.grid()
# plt.show()


# def wielo():
#     d=0
r=3
ff=0.01
zak=4.7
def fdz(x):
    a=x**4 + (5 + 1j)*x**3 - (8 - 5j)*x**2 + (30 - 14j)*x - 84
    return [a.real,
            a.imag]

odp_r=[]
odp_i=[]
y_r=[]
y_i=[]
for i in np.arange(-zak, zak, ff ):
    x1=fdz(i)
    y_r.append(x1[0])
    y_i.append(x1[1])
    if -0.15 <=round(x1[0],r)<=0.15:
        if  [round(x1[0],r)] not in odp_r:
            odp_r.append(round(i,r))
            #plt.plot((round(x1.x[0],r)), (round(x1.x[1],r)), 'o', color='r')
    if -0.15 <=round(x1[1],r)<=0.15:
        if  [round(x1[1],r)] not in odp_i:
            odp_i.append(round(i,r))
            plt.plot(round(i,r), round(x1[1],r), 'o', color='r')

print(odp_r)
print(odp_i)

# plt.set_xlim((0, 3))
# plt.set_ylim((0, 3))
x = np.arange(-zak, zak, ff )
plt.plot(x, y_r)
plt.plot(x, y_i)
plt.grid()
plt.show()