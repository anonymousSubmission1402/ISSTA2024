
def prime_factors(my_list):
    return set([i for i in range(2, int(math.sqrt(my_list[56])) + 1) if my_list[56] % i == 0 and math.gcd(i, my_list[56]) == 1])
