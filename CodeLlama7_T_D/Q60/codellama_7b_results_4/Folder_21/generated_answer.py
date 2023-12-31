
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current integer to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    # Return the sorted list of prime numbers
    return prime_list

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all integers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any integer between 2 and the square root of n, it is prime
    return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, it cannot be a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)))):
        # Remove the leading leftmost digit of n
        n = int(str(n)[1:])
        # Check if n is a prime number
        if not is_prime(n):
            # If n is not a prime number, it cannot be a left-and-right-truncatable prime number
            return False

    # If the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime, then n is a left-and-right-truncatable prime number
    return True
