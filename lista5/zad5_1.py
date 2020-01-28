#sigma obliczyć p 2,24 k=0,81
import matplotlib.pyplot as plt
import numpy as np
dx=np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7],dtype=float)
dy=np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828],dtype=float)

fk1 = np.polyfit(dx,dy, 1)
wiel1=np.poly1d(fk1)

fk2 = np.polyfit(dx,dy, 2)
wiel2=np.poly1d(fk2)
xx=np.arange(0.0, 4, 0.01)
plt.plot(xx, wiel1(xx))
plt.plot(xx, wiel2(xx))



plt.plot(dx, dy,'o')

plt.show()