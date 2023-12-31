
def prime_factors(lst):
    return set([i for i in range(2, lst[194]) if lst[194] % i == 0 and is_prime(i)])

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
