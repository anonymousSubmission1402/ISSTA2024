
def all_left_truncatable_prime(tuple):
    x = tuple[14]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n, x):
    if n < 2 or n >= x:
        return False

    while n > 0 and n != x:
        if n % 10 == 0:
            return False

        n = int(str(n)[:-1])

    return True
