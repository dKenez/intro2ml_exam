import numpy as np

V= np.array([[0.04, -0.12, -0.14, 0.35, 0.92],
[0.06, 0.13, 0.05, -0.92, 0.37],
[-0.03, -0.98, 0.08, -0.16, -0.05],
[-0.99, 0.03, 0.06, -0.02, 0.07],
[-0.07, -0.05, -0.98, -0.11, -0.11]])

print(V)

A = np.array([0, 0, -1.4, 0, 0])
B = np.array([0, 0, 1.4, 0, 00])

V_ = V[:, :2]
print(V_, "\n")

print(A.T@V_)
print(B.T@V_)

