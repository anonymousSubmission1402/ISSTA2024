
def all_right_truncatable_prime(tuple):
    x = tuple[36]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
