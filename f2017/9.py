import numpy as np


o1 = 5.7
o2 = 6
o3 = 6.2
o4 = 6.3
o5 = 6.4
o6 = 6.6
o7 = 6.7
o8 = 6.9
o9 = 7
o10 = 7.4


o = np.array([o1, o2, o3, o4, o5, o6, o7, o8, o9])

o10 = np.array(
    [o10])


o = np.array([
    [5.7],
    [2.91, 0.0, 3.23, 3.9, 2.88, 3.27, 3.48, 4.02, 3.08, 3.47],
    [0.63, 3.23, 0.0, 2.03, 1.06, 2.15, 2.11, 1.15, 1.09, 1.65],
    [1.88, 3.9, 2.03, 0.0, 2.52, 1.04, 2.25, 2.42, 2.18, 2.17],
    [1.02, 2.88, 1.06, 2.52, 0.0, 2.44, 2.38, 1.53, 1.71, 1.94],
    [1.82, 3.27, 2.15, 1.04, 2.44, 0.0, 1.93, 2.72, 1.98, 1.8],
    [1.92, 3.48, 2.11, 2.25, 2.38, 1.93, 0.0, 2.53, 2.09, 1.66],
    [1.58, 4.02, 1.15, 2.42, 1.53, 2.72, 2.53, 0.0, 1.68, 2.06],
    [1.08, 3.08, 1.09, 2.18, 1.71, 1.98, 2.09, 1.68, 0.0, 1.48],
    [1.43, 3.47, 1.65, 2.17, 1.94, 1.8, 1.66, 2.06, 1.48, 0.0]
])

def smallestN_indices(a, N):
    idx = a.ravel().argsort()[:N]
    return np.stack(np.unravel_index(idx, a.shape)).T

def density(obs, n, K):
    num = 1
    a = obs[:, n]

    indices = smallestN_indices(a, K+1)[1:].flatten()

    den = 0
    for i in indices:
        den += a[i]

    return K * num/den
    

def ard(obs, n, K):
    num = density(obs, n, K)

    a = obs[:, n]
    indices = smallestN_indices(a, K+1)[1:][:, 0].flatten()

    den = 0
    for i in indices:
        d = density(obs, i, K)
        den += d

    return K * num/den
    

print(ard(o, 3, 2))