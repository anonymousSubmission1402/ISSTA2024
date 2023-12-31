
def all_left_right_truncatable_prime(tuple):
    x = tuple[14]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and no_zeroes(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def no_zeroes(s):
    return '0' not in s
