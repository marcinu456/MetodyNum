import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def funM(x):
    return 3.5*x*(1-x)

X=[0]
Y=[0.1]
for i in range(100):
    Y.append(funM(Y[i]))
    X.append(i)
#plt.axis("equal")
print(len(X))
print(len(Y))
plt.scatter(X, Y)
plt.show()