
def prime_factors(my_list):
    return set([prime for prime in range(3, int(math.sqrt(my_list[24]) + 1)) if my_list[24] % prime == 0])
