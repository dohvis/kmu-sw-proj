def combination(n, r):
    if n == r or r == 0:
        return 1
    else:
        return combination(n-1, r) + combination(n-1, r-1)

get_n = int(input("Input n: "))
get_r = int(input("Input r: "))

if 0 <= get_r <= get_n:
    print(combination(get_n, get_r))
else:
    print("Range Error")