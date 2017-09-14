def factorial(num):

    if num == 0:
        return 1
    result = 1

    while num >= 1:
        result *= num
        num -= 1

    return result

def get_out_exception(num):
    try:
        num = int(num)
    except:
        print("Please put a integer")
        return 1

    if num < 0:
        print("Please put a integer ( >= 0)")
        return 1
    else:
        return 0;

print("If you type -1, the program ends")
while True:
    n = input("What is the n (n>=0)of 'n!': ")
    if n == '-1':
        break
    if get_out_exception(n) == 1:
        continue
    else:
        print(factorial(int(n)))
