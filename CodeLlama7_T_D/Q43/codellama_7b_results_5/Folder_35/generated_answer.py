
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(757, 968+1):
        is_prime = True
        for j in range(2, my_list[i]//2+1):
            if my_list[i] % j == 0:
                is_prime = False
                break

        if is_prime:

            prime_numbers.append(my_list[i])

    return sorted(prime_numbers, reverse=True)
