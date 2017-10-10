import time


def fibo_list(n):
    fibolist = [0, 1]
    for i in range(2, n + 1):
        fibolist.append(fibolist[i - 1] + fibolist[i - 2])
    return fibolist[n]
def fibo_value(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
def fibo_rec(n):
    if n<=1:
        return n
    return fiborec(n - 1) + fiborec(n - 2)
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
