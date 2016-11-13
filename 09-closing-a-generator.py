def numbers():
    s = 0
    while True:
        yield s
        s += 1


if __name__ == '__main__':
    numbers_gen = numbers()
    for i in range(10):
        print(next(numbers_gen))
    numbers_gen.close()

    # Raises an exception when someone wants to
    # access next element
    print(next(numbers_gen))
