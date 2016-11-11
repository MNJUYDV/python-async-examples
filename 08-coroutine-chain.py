def numbers():
    numbers_plus_1_gen = numbers_plus_1()
    next(numbers_plus_1_gen)

    while True:
        x = yield
        numbers_plus_1_gen.send(x)


def numbers_plus_1():
    numbers_plus_2_gen = numbers_plus_2()
    next(numbers_plus_2_gen)

    while True:
        x = yield
        x += 1
        numbers_plus_2_gen.send(x)


def numbers_plus_2():
    while True:
        x = yield
        x += 2
        print(x)


if __name__ == '__main__':
    numbers_gen = numbers()
    next(numbers_gen)
    for i in range(10):
        numbers_gen.send(i)
