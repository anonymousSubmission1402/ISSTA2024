
def all_left_right_truncatable_prime(tuple):
    x = tuple[975]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not any([0 in str(i), 0 in str(i)[::-1]]):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
