
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of positive integers
    for i in tuple:

        # Check if the integer is a prime number
        if is_prime(i):

            # If it is, check if it is left-and-right-truncatable prime
            if left_right_truncatable_prime(i):

                # If it is, add it to the list of prime numbers
                prime_numbers.append(i)

    return prime_numbers

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to n-1
        for i in range(2, n):

            # If n is divisible by any number between 2 and n-1, it is not prime
            if n % i == 0:

                return False

    return True

def left_right_truncatable_prime(n):

    # Check if n contains a 0 digit
    if '0' in str(n):

        # If it does, it is not left-and-right-truncatable prime
        return False

    # Get the digits of n in reverse order
    digits = list(reversed(str(n))))

    # Check if the leading digit is 1 or 2
    if digits[0] != '1' and digits[0] != '2':

        # If it is not, it is not left-and-right-truncatable prime
        return False

    # Remove the leading digit from the list of digits
    digits.pop(0)

    # Check if the remaining digits are equal to each other
    if len(set(digits)) == 1:

        # If they are, it is left-and-right-truncatable prime
        return True

    # If they are not, it is not left-and-right-truncatable prime
    return False
