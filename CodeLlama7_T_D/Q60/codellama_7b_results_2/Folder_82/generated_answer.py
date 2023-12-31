
def all_left_right_truncatable_prime(x):
    # Initialize the list of truncatable prime numbers
    truncatable_primes = []
    # Loop through the range of integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is a truncatable prime number
            if is_truncatable_prime(i):
                # Add the current integer to the list of truncatable prime numbers
                truncatable_primes.append(i)
    # Return the sorted list of truncatable prime numbers
    return sorted(truncatable_primes, reverse=True)
def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        # Return False if n is not a prime number
        return False

    # Initialize the list of factors

    factors = []

    # Loop through the range of integers from 2 to the square root of n

    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n

        if n % i == 0:
            # Add i to the list of factors

            factors.append(i)

    # Return False if the list of factors is not empty

    return len(factors) == 0

def is_truncatable_prime(n):
    # Check if n is a prime number

    if not is_prime(n):
        # Return False if n is not a prime number

        return False

    # Initialize the list of digits

    digits = []

    # Loop through the range of integers from 1 to the length of the representation of n in base 10

    for i in range(1, len(str(n)))):
        # Add the current digit to the list of digits

        digits.append(int(str(n))[i]))

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number

    for i in range(len(digits) - 1):
        # Check if the current digit is equal to the previous digit

        if digits[i] == digits[i - 1]:
            # Remove the leading leftmost and last rightmost digits from n

            n = int(str(n))[2:-2]))
            # Check if the resulting integer is a prime number

            if is_prime(n):
                # Return True if the current digit is equal to the previous digit and the resulting integer is a prime number

                return True

    # Return False if no left-and-right-truncatable prime number exists in the specified range

    return False
