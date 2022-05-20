import numpy as np

V = np.array([
    [0.45, -0.60, -0.64, 0.15],
    [-0.40, -0.80, 0.43, -0.16],
    [0.58, -0.01, 0.24, -0.78],
    [0.55, -0.08, 0.59, 0.58],
])

print(V)

X = np.array([-1, -1, -1, 1])

V_ = V[:, :2]
print(V_, "\n")

print(X_ := X.T@V)
print(X_[[0, 3]])
print(X_[[1, 3]])
print(X_[[1, 2]])
print(X_[[2, 3]])