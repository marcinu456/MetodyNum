import numpy as np
import matplotlib.pyplot as plt  

hm = [0,1.525,3.05,4.575,6.1,7.625,9.150]
#hm = [i * 100 for i in h]
p = [1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741]


fk1 = np.polyfit(hm,p,2)
#print(fk1)
wiel1 = np.poly1d(fk1)
xx = np.linspace(0,11,num=100, endpoint="True")
plt.plot(xx,wiel1(xx))
plt.plot(hm,p,'o')
print("P na wysokości h=10.5km = ", wiel1(10.5))
plt.show()
