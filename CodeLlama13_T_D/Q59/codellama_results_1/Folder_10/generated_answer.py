
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
