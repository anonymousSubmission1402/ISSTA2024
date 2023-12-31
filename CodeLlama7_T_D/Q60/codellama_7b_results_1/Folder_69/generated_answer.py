
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order and return it
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and it has no factors other than 1 and itself
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize an empty string to store the digits of n
    num_str = ""

    # Loop through all the digits of n
    for digit in str(n):
        # Check if the current digit is not 0
        if digit != "0":
            # Add the current digit to the string
            num_str += digit

    # Initialize a variable to store the number formed by concatenating the digits of n from left to right
    left_truncated_num = 0

    # Loop through all the digits of n from right to left
    for i in range(len(str(n)))):
        # Check if the current digit is not 0
        if str(n)[i] != "0":
            # Add the current digit to the number formed by concatenating the digits of n from left to right
            left_truncated_num = int(left_truncated_num * 10 + str(n)[i]))

    # Initialize a variable to store the number formed by concatenating the digits of n from right to left
    right_truncated_num = 0

    # Loop through all the digits of n from left to right
    for i in range(len(str(n))):
        # Check if the current digit is not 0
        if str(n)[i] != "0":
            # Add the current digit to the number formed by concatenating the digits of n from right to left
            right_truncated_num = int(right_truncated_num * 10 + str(n)[i]))

    # Check if the number formed by concatenating the digits of n from left to right is a prime number
    if is_prime(left_truncated_num):
        # Check if the number formed by concatenating the digits of n from right to left is a prime number
        if is_prime(right_truncated_num):
            # Return True if the number is both left-and-right-truncatable prime number and it remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            return True
