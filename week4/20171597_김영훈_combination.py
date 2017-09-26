def factorial(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    if n == r or r == 0:
        return 1
    else:
        return factorial(n) / (factorial(r) * factorial(n-r))

get_n = int(input("Input n: "))
get_r = int(input("Input r: "))

if 0 <= get_r <= get_n:
    print(combination(get_n, get_r))
else:
    print("Range Error")