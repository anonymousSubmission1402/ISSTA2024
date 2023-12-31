
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all integers from 1 to x, inclusive
    for i in range(1, x + 1):

        # Check if the current integer is a prime number
        if is_prime(i):

            # Check if the current integer is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current integer to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    # Return the sorted list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if n is prime
    if not is_prime(n):
        return False

    # Check if the leading leftmost digit of n is a prime number
    if not is_prime(int(str(n)[0]) + 1)):
        return False

    # Check if the last rightmost digit of n is a prime number
    if not is_prime(int(str(n))[-1] + 1)):
        return False

    # If the loop completes successfully, return True
    return True
