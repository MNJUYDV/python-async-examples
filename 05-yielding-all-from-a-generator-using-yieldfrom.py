def primes():
    p = [2,3,5,7,11,13,17,19]
    for i in p:
        yield i


def primes_again():
    prime_gen = primes()
    yield from prime_gen


if __name__ == '__main__':
    primes_again_gen = primes_again()
    for i in primes_again_gen:
        print(i)
