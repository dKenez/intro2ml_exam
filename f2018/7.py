from cmath import log, sqrt
import math
import numpy as np

pkm = np.array([
    [0.2, 0, 0.1],
    [0.3, 0.2, 0],
    [0.2, 0, 0]])

pk = np.sum(pkm, axis=1)
print(pk)

pm = np.sum(pkm, axis=0)
print(pm)


# pk = [4/9, 3/9, 2/9]
Hz = 0
for e in pk:
    Hz += -e*log(e, math.e)

print(f'{Hz=}')

# pm = [2/9, 2/9, 2/9, 3/9]
Hq = 0
for e in pm:
    Hq += -e*log(e, math.e)
print(f'{Hq=}')

# pkm = np.array([
#     [2/9, 2/9, 0, 0],
#     [0, 0, 2/9, 1/9],
#     [0, 0, 0, 2/9]])
Hzq = 0
for row in pkm:
    for e in row:
        if e != 0:
            Hzq += -e*log(e, math.e)
print(f'{Hzq=}')

MI = Hz + Hq - Hzq
print(f'{MI=}')
NMI = MI / (sqrt(Hz)*sqrt(Hq))  
print(f'{NMI=}') 