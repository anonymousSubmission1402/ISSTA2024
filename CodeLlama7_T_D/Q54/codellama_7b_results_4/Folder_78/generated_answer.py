
def all_right_truncatable_prime(tuple):
    # Get the integer at index 23 from the tuple
    x = tuple[23]

    # Initialize an empty list to store the right-truncatable prime numbers less than x

    rt_primes = []

    # Iterate from 1 to x

    for i in range(1, x + 1):

        # Check if i is a prime number

        if is_prime(i):

            # Check if the last rightmost digit of i is successively removed and still forms a prime number

            if is_right_truncatable_prime(i):

                # Add i to the list of right-truncatable prime numbers less than x

                rt_primes.append(i)

    # Sort the list of right-truncatable prime numbers less than x in ascending order

    return sorted(rt_primes)

# Define a function to check if a number is a prime number

def is_prime(n):

    # Check if n is greater than 1

    if n > 1:

        # Iterate from 2 to the square root of n

        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n

            if n % i == 0:

                # If i divides n, then n is not prime

                return False

    # If n is greater than 1, then it is prime

    return True

# Define a function to check if a number is a right-truncatable prime number

def is_right_truncatable_prime(n):

    # Check if n is a prime number

    if not is_prime(n):

        # If n is not a prime number, then it cannot be a right-truncatable prime number

        return False

    # Iterate from the length of the string representation of n to 1

    for i in range(len(str(n))), 1, -1):

        # Check if the last i digits of n form a prime number

        if is_prime(int(str(n)[0:(i)]))):

            # If the last i digits of n form a prime number, then n is a right-truncatable prime number

            return True

    # If no such i exists, then n is not a right-truncatable prime number

    return False
