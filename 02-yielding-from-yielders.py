def even():
    c = 0
    while True:
        yield c
        c += 2


def odd():
    c = 1
    while True:
        yield c
        c += 2


def natural():
    even_gen = even()
    odd_gen = odd()

    while True:
        yield next(even_gen)
        yield next(odd_gen)


if __name__ == '__main__':
    natural_gen = natural()
    for i in range(17):
        print(next(natural_gen))
