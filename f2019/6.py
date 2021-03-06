# o1 o2 o3 o4 o5 o6 o7 o8 o9 o10
# o1 0.0 4.2 8.3 3.9 3.8 4.6 6.3 4.8 7.1 4.9
# o2 4.2 0.0 7.4 2.6 3.0 3.2 5.3 3.1 6.6 4.6
# o3 8.3 7.4 0.0 6.3 7.1 5.5 2.8 5.4 2.4 5.3
# o4 3.9 2.6 6.3 0.0 1.5 1.6 4.1 1.8 5.3 2.4
# o5 3.8 3.0 7.1 1.5 0.0 2.4 4.9 2.8 5.8 3.2
# o6 4.6 3.2 5.5 1.6 2.4 0.0 3.7 1.7 4.8 2.3
# o7 6.3 5.3 2.8 4.1 4.9 3.7 0.0 3.8 1.9 3.6
# o8 4.8 3.1 5.4 1.8 2.8 1.7 3.8 0.0 4.9 2.1
# o9 7.1 6.6 2.4 5.3 5.8 4.8 1.9 4.9 0.0 4.4
# o10 4.9 4.6 5.3 2.4 3.2 2.3 3.6 2.1 4.4 0.0

import numpy as np

o = np.array([
[0.0, 4.2, 8.3, 3.9, 3.8, 4.6, 6.3, 4.8, 7.1, 4.9],
[4.2, 0.0, 7.4, 2.6, 3.0, 3.2, 5.3, 3.1, 6.6, 4.6],
[8.3, 7.4, 0.0, 6.3, 7.1, 5.5, 2.8, 5.4, 2.4, 5.3],
[3.9, 2.6, 6.3, 0.0, 1.5, 1.6, 4.1, 1.8, 5.3, 2.4],
[3.8, 3.0, 7.1, 1.5, 0.0, 2.4, 4.9, 2.8, 5.8, 3.2],
[4.6, 3.2, 5.5, 1.6, 2.4, 0.0, 3.7, 1.7, 4.8, 2.3],
[6.3, 5.3, 2.8, 4.1, 4.9, 3.7, 0.0, 3.8, 1.9, 3.6],
[4.8, 3.1, 5.4, 1.8, 2.8, 1.7, 3.8, 0.0, 4.9, 2.1],
[7.1, 6.6, 2.4, 5.3, 5.8, 4.8, 1.9, 4.9, 0.0, 4.4],
[4.9, 4.6, 5.3, 2.4, 3.2, 2.3, 3.6, 2.1, 4.4, 0.0]
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
    

print(ard(o, 4, 2))