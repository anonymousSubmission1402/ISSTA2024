
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Loop through each number in the tuple
    for num in tuple:
        # Check if the number is a prime number
        if is_prime(num):
            # If it is, check if it is left-truncatable prime
            if is_left_truncatable_prime(num):
                # If it is, add it to the result list
                result.append(num)
    # Return the result list sorted in descending order
    return sorted(result, reverse=True)

# Check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If it is, return False
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        # If it is, return False
        if n % i == 0:
            return False

    # If none of the above conditions are true, return True
    return True

# Check if a number is left-truncatable prime
def is_left_truncatable_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If it is, return False
        return False

    # Check if the leading leftmost digit of n is successively removed, then all resulting numbers are prime
    for i in range(len(str(n)))):
        # If any of the resulting numbers are not prime, return False
        if not is_prime(int(str(n)[i:]):
            return False

    # If none of the above conditions are true, return True
    return True
