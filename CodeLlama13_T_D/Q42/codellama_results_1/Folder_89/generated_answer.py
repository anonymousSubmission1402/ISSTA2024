
def prime_factors(numbers):
    return set(prime_factorization(numbers[18]))

def prime_factorization(n):
    if n == 1:
        return [1]
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return [p] + prime_factorization(n // p)
    return [n]
