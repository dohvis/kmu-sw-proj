def fibonacci_iterative(num):
    prev_1 = 0
    prev_2 = 1
    for i in range(0, num + 1):
        if i == 0:
            prev_1 = 0
        elif i == 1:
            prev_1 = 1
            prev_2 = 0
        else:
            tmp = prev_1
            prev_1 = prev_1 + prev_2
            prev_2 = tmp

    return prev_1
