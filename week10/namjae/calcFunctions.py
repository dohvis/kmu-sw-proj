def factorial(numStr):
    r = 1
    while numStr > 1:
        r *= numStr
        numStr -= 1
    return r


def decToBin(numStr):
    r = bin(numStr)
    return r


def binToDec(numStr):
    r = int(numStr, 2)
    return r


def decToRoman(numStr):
    r = numStr
    return r
