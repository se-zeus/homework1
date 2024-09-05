def __main__(num):
    s = ""
    for i in range(1, num):
        s += ("*" * i) + "\n"

    for i in range(0, num):
        s += ("*" * (num - i)) + "\n"

    return s


print(__main__(5))