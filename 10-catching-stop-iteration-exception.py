def numbers():
    for i in range(10):
        yield i


if __name__ == '__main__':
    numbers_gen = numbers()

    while True:
        try:
            val = next(numbers_gen)
        except StopIteration:
            print("Exiting infinite loop and closing the generator")
            numbers_gen.close()
            break
        else:
            print(val)
