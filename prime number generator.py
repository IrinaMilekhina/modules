def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

