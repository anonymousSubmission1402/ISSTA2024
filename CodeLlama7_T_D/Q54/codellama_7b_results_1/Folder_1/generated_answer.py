
def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[20]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    digits = [int(digit) for digit in str(n)]

    for i in range(len(digits) - 1, -1, -1):
        if n % 10 != 0 and n // 10 == int(str(n)[:-1]) * 10 + int(str(n)[-1])):
            return True

    return False
