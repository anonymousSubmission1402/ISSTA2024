
def all_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
