

import numpy as np

C = np.array([
    [114, 0, 32],
    [0, 119, 0],
    [8, 0, 60],
])

S = 0

for row in C:
    for e in row:
        S += e * (e-1)/2

print(f'{S=}')

N_pairs = np.sum(C)*(np.sum(C)-1)/2

D = N_pairs

sums = [np.sum(C, axis=1), np.sum(C, axis=0)]

for asum in sums:
    for class_sum in asum:
        D -= class_sum*(class_sum-1)/2

D += S

print(f'{D=}')

rand = (S+D)/N_pairs
print(f'{rand=}')