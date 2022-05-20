def var(num, den):
    a = 0
    for s in num:
        a += s**2

    b = 0
    for s in den:
        b += s**2

    return a/b

den = [30.19, 16.08, 11.07, 5.98]
numA = den[:1]
numB = den[:2]
numC = den[:3]
numD = den[-1:]

print(f'A: {var(numA, den)*100}%')
print(f'B: {var(numB, den)*100}%')
print(f'C: {var(numC, den)*100}%')
print(f'D: {var(numD, den)*100}%')