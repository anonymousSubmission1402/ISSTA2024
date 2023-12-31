 def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than x

    for num in range(1, x + 1):

        # Check if num is a prime number

        if is_prime(num):

            # If num is a prime number, check if it is right-truncatable

            if is_right_truncatable(num):

                # If num is both a prime number and a right-truncatable prime number, add it to the list of prime numbers

                prime_numbers.append(num)

    # Sort the list of prime numbers in ascending order

    sorted_prime_numbers = sorted(prime_numbers)

    # Return the sorted list of prime numbers

    return sorted_prime_numbers

# Define a function to check if a number is a prime number

def is_prime(n):

    # Check if n is equal to 1 or less than 2

    if n <= 1:

        # If n is equal to 1 or less than 2, return False

        return False

    # Loop through all numbers up to and including the square root of n

    for i in range(2, int(n ** 0.5) + 1):

        # Check if i divides n

        if n % i == 0:

            # If i divides n, return False

            return False

    # If n is a prime number, return True

    return True

# Define a function to check if a right-truncatable prime number remains prime when the last rightmost digit is successively removed

def is_right_truncatable(n):

    # Loop through all numbers up to and including the last two digits of n

    for i in range(len(str(n))) - 2, len(str(n)) - 1):

        # Check if the number formed by removing the rightmost digit of n is equal to 1 or less than 2

        if int(str(n)[0:i]) <= 1:

            # If the number formed by removing the rightmost digit of n is equal to 1 or less than 2, return False

            return False

    # If n is a right-truncatable prime number, return True

    return True
