
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(21, 98):
        if my_list[i] == 1:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
