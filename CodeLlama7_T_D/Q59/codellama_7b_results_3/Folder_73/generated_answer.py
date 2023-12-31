 def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[97]
    list_of_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if n < 10:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

        if len(str(n)) > 1 and str(n)[0] != "1" and n % int(str(n)[0]) == 0:
            return False

    return True
