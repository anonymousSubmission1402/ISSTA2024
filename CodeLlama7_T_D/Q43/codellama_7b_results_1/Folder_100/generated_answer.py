
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers from index 18 to index 59
    for i in range(18, 60):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If the current number is divisible by any number between 2 and the square root of the current number, it is not prime
                break

        else:

            # If the loop completes without breaking, the current number is prime
            prime_numbers.append(i)

    return sorted(prime_numbers)
