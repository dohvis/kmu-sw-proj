def f(num):
    return (num * f(num-1)) if num > 1 else 1


while True:
    num = input('Input integer: ')
    print(f(num))
