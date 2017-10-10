import time

def iterfibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    get_num = int(input("Enter a number: "))
    if get_num == -1:
        break
    # iterfibo function
    ts = time.time()
    fibo_result = iterfibo(get_num)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" % (get_num, fibo_result, ts))
    # fibo function
    ts = time.time()
    fibo_result = fibo(get_num)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" % (get_num, fibo_result, ts))