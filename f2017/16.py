import numpy as np

x = np.array([6.8, 225, 0.44, 0.68])

b_0 = 2.84
b_11 = 3.25
b_12 = 3.46

w_1 = np.array([21.78, -1.65, 0, -13.26, -8.46])
w_2 = np.array([-9.60, -0.44, 0.01, 14.54, 9.50])


def h(x): return max(x, 0)


res = b_0 + (b_11 * h(np.insert(x, 0, 1)@w_1)) + \
    (b_12 * h(np.insert(x, 0, 1)@w_2))

print(res)
