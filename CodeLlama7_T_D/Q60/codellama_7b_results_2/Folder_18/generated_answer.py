
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all integers from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # If it is, check if it is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # If it is, add it to the list of prime numbers
                prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Check if n is a prime number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
