
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[89]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(n):
    if n <= 1 or not isinstance(n, int):
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
