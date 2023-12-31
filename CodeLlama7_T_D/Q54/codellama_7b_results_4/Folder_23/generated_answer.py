
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through the tuple of positive integers
    for i in range(len(tuple)):

        # Check if the current number is a prime number
        if is_prime(tuple[i]):

            # If the current number is a prime number, add it to the list of prime numbers
            prime_numbers.append(tuple[i])

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers, reverse=True)

# Check if a given integer is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through the numbers from 2 to n-1
        for i in range(2, n):

            # If the remainder of n/i is 0, return False
            if n % i == 0:
                return False

    # If the number is greater than 1, return True
    if n > 1:
        return True

# If the number is less than or equal to 1, return False
if n <= 1:
    return False
