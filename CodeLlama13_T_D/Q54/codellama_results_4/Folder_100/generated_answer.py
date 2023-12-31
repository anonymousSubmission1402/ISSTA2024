
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[26]
    right_truncatable_primes = []
    for i in range(10, x+1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
