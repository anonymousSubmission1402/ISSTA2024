
def prime_factors(my_list):
    prime_factor_set = set()
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) + 1):
                if my_list[i] % j == 0:
                    prime_factor_set.add(j)
    return prime_factor_set
