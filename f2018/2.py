def var(num, den):
    a = 0
    for s in num:
        a += s**2

    b = 0
    for s in den:
        b += s**2

    return a/b

den = [14.4, 8.19, 7.83, 6.91, 6.01]
numA = [14.4]
numB = [14.4, 8.19, 7.83, 6.91]
numC = [8.19, 7.83, 6.91, 6.01]
numD = [14.4, 8.19, 7.83]

print(f'A: {var(numA, den)}')
print(f'B: {var(numB, den)}')
print(f'C: {var(numC, den)}')
print(f'D: {var(numD, den)}')