
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (exclusive)
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n (exclusive)
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # If the loop completes, return True if n is greater than 1, else return False
    return n > 1

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains no 0
    if '0' not in str(n):
        # Iterate from the leading leftmost digit to the last rightmost digit (exclusive)
        for i in range(len(str(n)))):
            # Check if removing the current digit from both the left and right sides of the number still produces a prime number
            if is_prime(int(str(n)[i + 1:]))) and is_prime(int(str(n)[:-i - 1])))
                # Return True if removing the current digit from both the left and right sides of the number still produces a prime number
                return True

    # If the loop completes, return False if the number contains no 0 or if removing the current digit from both the left and right sides of the number does not produce a prime number
    return False
