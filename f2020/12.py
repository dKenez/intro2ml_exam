import numpy as np

o = np.array([
    [0, 725, 800, 150, 1000, 525, 600, 500, 400, 850],
    [725, 0, 75, 575, 275, 1250, 1325, 226, 325, 125],
    [800, 75, 0, 650, 200, 1325, 1400, 300, 400, 51],
    [150, 575, 650, 0, 850, 675, 750, 350, 250, 700],
    [1000, 275, 200, 850, 0, 1525, 1600, 500, 600, 150],
    [525, 1250, 1325, 675, 1525, 0, 75, 1025, 925, 1375],
    [600, 1325, 1400, 750, 1600, 75, 0, 1100, 1000, 1450],
    [500, 226, 300, 350, 500, 1025, 1100, 0, 100, 350],
    [400, 325, 400, 250, 600, 925, 1000, 100, 0, 450],
    [850, 125, 51, 700, 150, 1375, 1450, 350, 450, 0],
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


print(ard(o, 1, 2))
