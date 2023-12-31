
def find_primes_between_indices(list_of_integers):
    return sorted([x for x in list_of_integers[497:931] if is_prime(x)], reverse=True)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
