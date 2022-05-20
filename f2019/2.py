def var(num, den):
    a = 0
    for s in num:
        a += s**2

    b = 0
    for s in den:
        b += s**2

    return a/b

den = [43.67, 33.47, 31.15, 30.36, 27.77, 13.86]
numA = [43.67, 33.47, 31.15, 30.36, 27.77]
numB = [43.67, 33.47, 31.15]
numC = [43.67]
numD = [27.77, 13.86]

print(f'A: {var(numA, den)}')
print(f'B: {var(numB, den)}')
print(f'C: {var(numC, den)}')
print(f'D: {var(numD, den)}')