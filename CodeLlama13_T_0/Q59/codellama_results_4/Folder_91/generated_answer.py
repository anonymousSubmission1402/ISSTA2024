
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10**(len(str(x))-1), x+1):
        if is_prime(i) and not any(map(lambda n: str(n).startswith('0'), range(2, int(str(i)[1:])))
            primes.append(i)
    return sorted(primes, reverse=True)
