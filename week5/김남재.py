import time


def fibo_list(n):
    fibolist = [0, 1]
    for i in range(1, n):
        fibolist.append(fibolist[i] + fibolist[i - 1])
    return fibolist[n]
def fibo_value(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
def fibo_rec(n):
    if n<=1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)
def profile(func, nbr):
    ts = time.time()
    fibonum = func(nbr)
    ts = time.time() - ts
    print("%s(%d)=%d, time %.6f" % (func.__name__, nbr, fibonum, ts))

while True:
    try:
        nbr = int(input("Enter a number: "))
    except ValueError:
        print("Only int")
        continue
    if nbr == -1:
        break
    profile(fibo_list, nbr)
    profile(fibo_value, nbr)
    profile(fibo_rec, nbr)
