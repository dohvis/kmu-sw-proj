def factorial(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

while True:
    try:
        getNum = int(input("Enter a number: "))
    except ValueError:
        print("Please enter only a integer !!")
    else:
        if getNum == -1:
            break
        elif getNum == 0:
            print("0! = 1")
        elif getNum < -1:
            print("Do not enter the negative number except -1")
        else:
            result = factorial(getNum)
            print("%d! = %d" %(getNum,result))