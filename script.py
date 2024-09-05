def __main__(num):

    for i in range(1, num):
        print("*" * i)

    for i in range(0, num):
        print("*" * (num - i))


__main__(5)