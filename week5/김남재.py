def fibo(n):
    fibolist = [0, 1]
    for i in range(2, n+1):
        fibolist.append(fibolist[i-1] + fibolist[i-2])
    return fibolist[n]

for i in range(0, 100):
    print(fibo(i))
