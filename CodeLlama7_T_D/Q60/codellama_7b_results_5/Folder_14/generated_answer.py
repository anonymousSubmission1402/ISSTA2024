
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through the tuple elements
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Check if the element is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(element):
                # Add the element to the list of prime numbers
                prime_list.append(element)
    return prime_list

def is_prime(n):
    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:
        return False

    # Check if n is a multiple of 2 to n - 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the loop completes, then n is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:
        return False

    # Convert n to a string
    n_str = str(n)

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, len(n_str)):
        # Remove the leading leftmost digit
        leftmost_removed = int(n_str[i:])
        # Check if the number is prime
        if is_prime(leftmost_removed):
            # Check if the last rightmost digit can be removed without losing primality
            if len(str(leftmost_removed)) > 1:
                # Remove the last rightmost digit
                last_rightmost_removed = int(str(leftmost_removed)[:-1]))
                # Check if the number is prime
                if is_prime(last_rightmost_removed):
                    # If the loop completes, then n is a left-and-right-truncatable prime number
                    return True

    # If the loop completes, then n is not a left-and-right-truncatable prime number
    return False
