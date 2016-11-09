def primes():
    p = [2,3,5,7,11,13,17,19]
    for i in p:
        yield i


def prime_plus_2():
    prime_gen = primes()
    for prime_number in prime_gen:
        yield (prime_number + 2)


if __name__ == '__main__':
    prime_puls_2_gen = prime_plus_2()
    for i in prime_puls_2_gen:
        print(i)
