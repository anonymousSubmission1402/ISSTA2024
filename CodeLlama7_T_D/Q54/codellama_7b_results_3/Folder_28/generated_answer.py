 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    rtprimes = []
    # Iterate over each element in the tuple
    for i in range(len(tuple)):
        x = tuple[i]
        # Check if x is a prime number
        if is_prime(x):
            # Check if x is a right-truncatable prime number
            if is_right_truncatable_prime(x):
                # Add x to the list of right-truncatable prime numbers
                rtprimes.append(x)
    # Sort the list of right-truncatable prime numbers in ascending order
    rtprimes = sorted(rtprimes)
    # Return the sorted list of right-truncatable prime numbers
    return rtprimes

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n - 1
        i = n - 1
        # Iterate while i is greater than 1
        while i > 1:
            # Check if i is divisible by n
            if i % n == 0:
                # Return False since n is not a prime number
                return False

            # Decrement i by 1
            i -= 1

    # If n is less than or equal to 1, return False
    else:
        return False

def is_right_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n - 1
        i = n - 1
        # Iterate while i is greater than 1
        while i > 1:
            # Check if i is divisible by n
            if i % n == 0:
                # Return True since n is a right-truncatable prime number
                return True

            # Decrement i by 1
            i -= 1

    # If n is less than or equal to 1, return False
    else:
        return False
