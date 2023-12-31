
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime
    is_prime = lambda x: x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
    # Find the indices of the first and last prime numbers in the list
    first_prime_index = next((i for i, x in enumerate(my_list) if is_prime(x)) or None)
    last_prime_index = next((i for i, x in enumerate(reversed(my_list))) if is_prime(x))
    # Return the sorted list of prime numbers between the indices
    return sorted([my_list[i] for i in range(first_prime_index, last_prime_index + 1)])
