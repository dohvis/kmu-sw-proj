def factorial(num):
    return (num * factorial(num-1)) if num > 1 else 1

def combination(n, r):
    # return factorial(n) / (factorial(n) * (n-r))
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError('Not int')
    if (n < r):
        raise ValueError('n < r')
    if n < 1 or r < 0:
        print(n, r)
        raise ValueError('{n} < 1,  {r} < 0'.format(n=n, r=r))
    r = min(r, n - r)
    return 1 if n == r or r == 0 else combination(n-1, r-1) + combination(n-1, r)

print(combination(3, 2))

