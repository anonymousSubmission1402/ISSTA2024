
def all_left_truncatable_prime(numbers):
    x = numbers[23]
    prime_list = []
    for i in range(10**x):
        if is_prime(i) and not '0' in str(i):
            prime_list.append(i)
    return sorted(prime_list)
