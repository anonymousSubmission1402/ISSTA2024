
def all_left_truncatable_prime(numbers):
    x = numbers[25]
    prime_list = []
    for i in range(10, x):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
