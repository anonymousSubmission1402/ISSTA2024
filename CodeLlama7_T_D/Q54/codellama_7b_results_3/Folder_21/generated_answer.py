 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []
    # Iterate over the elements in the tuple
    for i in range(len(tuple)):
        # Get the current element in the tuple
        current_element = tuple[i]
        # Check if the current element is a prime number
        if is_prime(current_element):
            # If it is a prime number, check if it is right-truncatable prime number
            if is_right_truncatable_prime(current_element):
                # If it is a right-truncatable prime number, add it to the result list
                result.append(current_element)
    # Sort the result list in ascending order
    result.sort()
    return result

def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, it cannot be a right-truncatable prime number
        return False

    # Check if the last rightmost digit of n is 1
    if n % 10 == 1:
        # If the last rightmost digit of n is 1, it is a right-truncatable prime number
        return True

    # Check if the last rightmost digit of n is 3 or 7
    elif n % 10 in [3, 7]:
        # If the last rightmost digit of n is 3 or 7, it is a right-truncatable prime number
        return True

    # Otherwise, it is not a right-truncatable prime number
    else:
        return False

def is_prime(n):
    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n <= 1:
        # If n is not an integer greater than 1, it is not a prime number
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # If n is divisible by i, it is not a prime number
        if n % i == 0:
            return False

    # Otherwise, it is a prime number
    else:
        return True
