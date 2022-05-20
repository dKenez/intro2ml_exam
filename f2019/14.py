import enum
import numpy as np

def E(x, y, w, l):
    E_y = np.average(y)

    y_ = ((x - np.average(x)) / np.std(x, ddof=1))*w + E_y

    s = 0

    for i, (yi, yi_) in enumerate(zip(y, y_)):
        s += (yi - yi_)**2

    return s + l*(w.T@w)

x = np.array([2, 5, 6, 7])
y = np.array([6, 7, 7, 9])

x_ = (x - np.average(x)) / np.std(x)

w = np.array([0.6])
l = 2

print(E(x, y, w, l))

# w_0 = np.average(y)
# y_ = y - w_0


# E = (y_ - x_*w).T@(y_ - x_*w) - l*w**2
# print(E)

