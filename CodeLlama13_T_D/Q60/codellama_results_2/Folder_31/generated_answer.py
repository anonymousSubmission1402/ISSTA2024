
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n) and is_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if len(str(n)) <= 2:
        return True
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True
