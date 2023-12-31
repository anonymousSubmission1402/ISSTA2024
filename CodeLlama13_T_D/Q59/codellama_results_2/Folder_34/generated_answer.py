
def all_left_truncatable_prime(x):
    x = list(range(1, x+1))
    prime_numbers = []
    for num in x:
        if is_prime(num) and not "0" in str(num):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)
