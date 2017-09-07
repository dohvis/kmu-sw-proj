def factorial(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res

number = 0

while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter only a integer !!")
    else:
        if number == -1:
            break
        elif number == 0:
            print("0! = 1")
        elif number < -1:
            print("Do not enter the negative number except -1")
        else:
            result = factorial(number)
            print("%d! = %d" %(number,result))
