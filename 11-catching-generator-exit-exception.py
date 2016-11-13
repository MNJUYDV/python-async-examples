def numbers():
    try:
        for i in range(10):
            yield i
    except GeneratorExit:
        print("Exiting the generator")


if __name__ == '__main__':
    numbers_gen = numbers()
    print(next(numbers_gen))

    # Raises the GeneratorExit exception inside the generator
    numbers_gen.close()
