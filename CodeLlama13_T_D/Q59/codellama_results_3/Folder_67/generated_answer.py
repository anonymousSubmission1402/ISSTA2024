
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    left_truncatable_primes = []
    for p in primes:
        while len(str(p)) > 1:
            p = int(str(p)[1:])
            if not is_prime(p):
                break
            else:
                left_truncatable_primes.append(p)
    
    return sorted(left_truncatable_primes, reverse=True)
