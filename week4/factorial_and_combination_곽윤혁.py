import math


def factorial(num):
    if not isinstance(num, int):
        raise ValueError('num must be a integer')
    if num < 0:
        raise ValueError('num must be bigger than 0')
    if num == 0:
        return 1
    return num * factorial(num - 1)


def combination_by_factorial(n, r):
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError('Not int')
    if n < r:
        raise ValueError('n < r')
    if n < 1 or r < 0:
        print(n, r)
        raise ValueError('{n} < 1,  {r} < 0'.format(n=n, r=r))
    r = min(r, n-r)
    # a combination nCr is equal to n! / r! * (n-r)!
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def combination_by_recursive(n, r):
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError('Not int')
    if n < r:
        raise ValueError('n < r')
    if n < 1 or r < 0:
        print(n, r)
        raise ValueError('{n} < 1,  {r} < 0'.format(n=n, r=r))
    r = min(r, n - r)
    if r == 0:
        return 1
    if r == 1:
        return n
    # a combination nCr is equal to n-1Cr-1 + n-1Cr
    return combination_by_recursive(n - 1, r - 1) + combination_by_recursive(n - 1, r)


print(combination_by_factorial(25, 13))
print(combination_by_recursive(25, 13))
