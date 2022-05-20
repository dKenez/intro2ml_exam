import numpy as np


LOW = -1
HIGH = 1

V = np.array([[0.1, -0.45, -0.55, 0.67, -0.2, 0.01],
              [-0.63, -0.02, -0.01, -0.05, -0.44, -0.64],
              [-0.67, 0.07, 0.03, 0.13, -0.12, 0.72],
              [-0.09, 0.69, 0.03, 0.6, 0.32, -0.2],
              [0.06, -0.35, 0.83, 0.41, -0.09, -0.03],
              [0.37, 0.44, 0.05, 0.04, -0.8, 0.17]])

print(V)

# x1 = MONTH
# x3 = PM10
# x5 = CO
# x8 = PRES
# x10 = RAIN
# x11 = WSPM

A = np.array([0, LOW, 0, HIGH, 0, LOW])
B = np.array([0, HIGH, HIGH, 0, 0, LOW])
C = np.array([LOW, 0, 0, LOW, LOW, 0])
D = np.array([HIGH, 0, 0, 0, LOW, 0])

V_A = V[:, 4]
V_B = V[:, 0]
V_C = V[:, 3]
V_D = V[:, 2]

# print(V_A, V_B, V_C, V_D)

print(A.T@V_A)
print(B.T@V_B)
print(C.T@V_C)
print(D.T@V_D)
