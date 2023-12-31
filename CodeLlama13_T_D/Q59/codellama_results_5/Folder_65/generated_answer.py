
def all_left_truncatable_prime(tuple):
    x = tuple[32]
    prime_list = []
    for i in range(2,x+1):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
    left_truncatable_prime_list = []
    for j in prime_list:
        if all([is_prime(j[1:]) for j in str(j)]):
            left_truncatable_prime_list.append(j)
    return sorted(left_truncatable_prime_list)
