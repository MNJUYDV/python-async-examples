def sum_coroutine():
    while True:
        x, y = (yield)
        print(x + y)


if __name__ == '__main__':
    s = sum_coroutine()
    next(s)

    s.send((1, 2))
    s.send((4, 5))
    s.send((11, 9))
