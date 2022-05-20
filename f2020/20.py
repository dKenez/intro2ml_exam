from random import random
import numpy as np
import matplotlib.pyplot as plt

def norm1(p):
    d = 0
    for c in p: d += abs(c)
    return d

N = 4000

x_1 = []
y_1 = []

x_2 = []
y_2 = []

x_3 = []
y_3 = []

def t_1(p):
    if norm1(p-np.array([2, 4])) < 3:
        if norm1(p-np.array([4, 2])) < 3:
            return 2
        else: return 1
    else:
        if norm1(p-np.array([6, 4])) < 3:
            return 3
        else: return 1

def t_2(p):
    if norm1(p-np.array([6, 4])) < 3:
        if norm1(p-np.array([2, 4])) < 3:
            return 2
        else: return 1
    else:
        if norm1(p-np.array([4, 2])) < 3:
            return 3
        else: return 1

def t_3(p):
    if norm1(p-np.array([6, 4])) < 3:
        if norm1(p-np.array([4, 2])) < 3:
            return 2
        else: return 1
    else:
        if norm1(p-np.array([2, 4])) < 3:
            return 3
        else: return 1

def t_4(p):
    if norm1(p-np.array([2, 4])) < 3:
        if norm1(p-np.array([6, 4])) < 3:
            return 2
        else: return 1
    else:
        if norm1(p-np.array([4, 2])) < 3:
            return 3
        else: return 1

for _ in range(N):
    p = np.array([random() * 6, random() * 6])

    c = t_2(p)

    match c:
        case 1:
            x_1.append(p[0])
            y_1.append(p[1])
        case 2:
            x_2.append(p[0])
            y_2.append(p[1])
        case 3:
            x_3.append(p[0])
            y_3.append(p[1])
    

plt.scatter(x_1, y_1, c='b', marker='o', label='1')
plt.scatter(x_2, y_2, c='r', marker='x', label='2')
plt.scatter(x_3, y_3, c='y', marker='s', label='3')
plt.legend(loc='upper left')
plt.show()