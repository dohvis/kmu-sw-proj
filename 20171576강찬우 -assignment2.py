num = int(input("Enter a number:  "))
while num != -1:
    k = 1

    for i in range(1,num+1):
        k *= i
    print("%d! = %d" %(num,k))
    num = int(input("Enter a number:  "))
    continue



