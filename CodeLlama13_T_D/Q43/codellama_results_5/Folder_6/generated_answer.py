
def find_primes_between_indices(my_list):
    primes = []
    for i in range(89, 94):
        if my_list[i] in primes:
            continue
        else:
            primes.append(my_list[i])
    return sorted(primes, reverse=True)
