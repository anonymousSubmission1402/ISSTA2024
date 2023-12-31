
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the numbers less than or equal to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list
                prime_numbers.append(num)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the numbers less than n
        for i in range(2, n):

            # Check if i divides n without a remainder
            if n % i == 0:

                # Return False since n is not prime
                return False

    # Return True since n is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains 0
    if '0' in str(n):

        # Return False since the number contains 0
        return False

    # Initialize an empty string to store the leading leftmost and last rightmost digits of the number
    leading_leftmost = ''
    last_rightmost = ''

    # Loop through all the numbers less than n
    for i in range(2, n):

        # Check if i divides n without a remainder
        if n % i == 0:

            # Update the leading leftmost and last rightmost digits of the number
            leading_leftmost = str(i) + leading_leftmost
            last_rightmost = last_rightmost + str(i)

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    if len(leading_leftmost) == 1 or len(last_rightmost) == 1:

        # Return True since the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
        return True

    # Check if the number is still prime after removing the leading leftmost and last rightmost digits
    else:

        # Update the number by removing the leading leftmost and last rightmost digits
        n = n // int(leading_leftmost) // int(last_rightmost)

        # Check if the updated number is prime
        if is_prime(n):

            # Return True since the number is still prime after removing the leading leftmost and last rightmost digits
            return True

    # Return False since the number is not a left-and-right-truncatable prime number
    return False
