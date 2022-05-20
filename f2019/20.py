from math import exp
import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1/(1+exp(-x))


x = np.array([6.8, 225, 0.44, 0.68])

b_0 = 1.4

w_11 = np.array([-0.5, -0.1])
w_12 = np.array([0.9, 2])

w_2 = np.array([-1, 0.4])


def h(x): return sigmoid(x)

def f(x): 
    return h(b_0 + w_2[0] * h(np.insert(np.array([x]), 0, 1)@w_11) + w_2[1]*h(np.insert(np.array([x]), 0, 1)@w_12)) 

x = []
y = []


f_v = np.vectorize(f)
x = np.linspace(-2, 2, num=100)
y = f_v(x)

print(x)
print(y)

plt.plot(x, y)
plt.show()