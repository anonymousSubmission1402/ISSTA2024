
def find_primes_between_indices(my_list):
    primes = []
    for i in range(239, 687):
        if my_list[i] % 2 == 0 and my_list[i] != 2:
            continue
        else:
            primes.append(my_list[i])
    return sorted(primes)
