
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(295, 456):
        if my_list[i] in prime_numbers:
            continue
        is_prime = True
        for j in range(2, int(my_list[i]**0.5) + 1):
            if my_list[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
