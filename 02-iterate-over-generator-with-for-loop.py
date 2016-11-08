def even_numbers():
    for i in range(0, 11, 2):
        yield i


if __name__ == '__main__':
    evens = even_numbers()
    for i in evens:
        print(i)
