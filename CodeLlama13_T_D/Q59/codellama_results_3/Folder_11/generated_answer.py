
def all_left_truncatable_prime(tuple):
    x = tuple[86]
    prime_list = []
    for i in range(10**x):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
    
    return sorted(prime_list)
