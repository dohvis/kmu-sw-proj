def f(num):
    return (num * f(num-1)) if num > 1 else 1

def c(n, r):
    # return f(n) / (f(n) * (n-r))
    return  1 if n == r or r == 0 else c(n-1, r-1) + c(n-1, r)

print(c(10, 3))

