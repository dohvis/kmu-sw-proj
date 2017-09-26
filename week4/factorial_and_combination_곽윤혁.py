import math


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def combination_by_factorial(num, r):
    # a combination nCr is equal to n! / r! * (n-r)!
    return int(math.factorial(num) / (math.factorial(r) * math.factorial(num - r)))


def combination_by_recursive(num, r):
    r = min(r, num - r)
    if r == 0:
        return 1
    if r == 1:
        return num
    # a combination nCr is equal to n-1Cr-1 + n-1Cr
    return combination_by_recursive(num - 1, r - 1) + combination_by_recursive(num - 1, r)


print(combination_by_factorial(25, 13))
print(combination_by_recursive(25, 13))
