
def find_primes_between_indices(list):
    primes = []
    for i in range(1, len(list)):
        if is_prime(list[i]):
            primes.append(list[i])
    return sorted(primes)
