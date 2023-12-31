
def all_right_truncatable_prime(numbers):
    x = numbers[26]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
