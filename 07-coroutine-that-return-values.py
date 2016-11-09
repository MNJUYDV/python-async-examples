def sum_coroutine():
    s = yield
    while True:
        x = yield s
        s += x


if __name__ == '__main__':
    s = sum_coroutine()
    next(s)

    print(s.send(1))
    print(s.send(4))
    print(s.send(1))
