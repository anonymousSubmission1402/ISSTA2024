
def all_left_truncatable_prime(tuple):
    x = tuple[175]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)
