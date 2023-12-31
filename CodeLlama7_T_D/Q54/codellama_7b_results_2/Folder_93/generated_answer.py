
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the tuple elements
    for element in tuple:

        # Check if the current element is a prime number
        if is_prime(element):

            # Store the current element as a prime number
            prime_numbers.append(element)

    return sorted(prime_numbers, key=lambda x: x)

def is_prime(n):

    # Check if n is less than 2
    if n < 2:

        # Return False if n is less than 2
        return False

    # Loop through the numbers from 2 to n-1
    for i in range(2, n):

        # Check if n % i is equal to 0
        if n % i == 0:

            # Return False if n % i is equal to 0
            return False

    # If the loop completes successfully, return True
    return True
