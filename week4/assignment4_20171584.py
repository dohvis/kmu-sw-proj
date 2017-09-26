def fac(num):
    if num==1 or num==0:
        return 1
    elif num < 0:
        return -1
    else:
        return num * fac(num-1)
def combination(n, r):
    #res1 = fac(n) / (fac(r) * fac(n-r))
    if r==n or r==0:
        return 1
    if n<r:
        return -1
    else:
        return combination(n-1, r-1) + combination(n-1, r)

while True:
    n = int(input("input n : "))
    r = int(input("input r : "))
    if n==-1:
        break
    print(combination(n,r))
