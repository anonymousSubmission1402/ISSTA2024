
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(69, 84+1):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)
