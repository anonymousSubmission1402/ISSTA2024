
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') or str(i)[-1] == '0' for _ in range(len(str(i)) - 1)):
            primes.append(i)
    return sorted(primes, reverse=True)
