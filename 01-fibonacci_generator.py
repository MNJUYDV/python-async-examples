"""
Infinitely generate finonacci numbers using generators
"""

def fib():
    f0, f1 = 0, 1
    while True:
        f = f0 + f1
        yield f
        f0, f1 = f1, f


if __name__ == '__main__':
    fib_generator = fib()

    # Prints first 10 fibonacci numbers using generators
    for i in range(10):
        f = next(fib_generator)
        print(f)
