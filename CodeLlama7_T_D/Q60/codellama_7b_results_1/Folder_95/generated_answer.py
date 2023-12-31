
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)
    return prime_list

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")
    # Check if n is an odd number
    if n % 2 == 0:
        return False

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    leading_leftmost_digits = str(n)[0:-1]
    last_rightmost_digits = str(n)[:-1]

    for i in range(len(leading_leftmost_digits)):
        if not is_prime(int(leading_leftmost_digits[i:])):
            return False

    for i in range(len(last_rightmost_digits)):
        if not is_prime(int(last_rightmost_digits[-i:])))
            return False

    # If the number satisfies all the conditions, it is a left-and-right-truncatable prime number
    return True
