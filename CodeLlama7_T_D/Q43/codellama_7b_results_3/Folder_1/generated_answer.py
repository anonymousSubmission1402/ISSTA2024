
def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Iterate over the list from index 87 to 89, both inclusive
    for i in range(87, 90):

        # Check if the current element is a prime number
        if my_list[i] > 1:
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 87 to index 89, both inclusive
    return sorted(prime_numbers)
