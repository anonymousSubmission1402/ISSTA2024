
def all_left_truncatable_prime(tuple):
    # Extract the integer at index 433 from the tuple
    x = tuple[433]
    # Initialize an empty list to store the results
    result = []

    # Iterate over the numbers less than x and check if they are left-truncatable prime numbers
    for i in range(1, x):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number can be obtained by removing leading digits successively
            if remove_leading_digits(i) == []:
                result.append(i)
    return sorted(result, reverse=True)
