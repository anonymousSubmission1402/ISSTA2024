
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through each number in the tuple
    for num in tuple:
        # Check if the number is prime
        if is_prime(num):
            # If it is prime, check if it is left-truncatable
            if is_left_truncatable_prime(num):
                # If it is, add it to the list of prime numbers
                prime_list.append(num)
    return sorted(prime_list, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers from 2 to n-1
        for i in range(2, n):
            # If n is divisible by any number other than 1 and itself, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True

# Define a function to check if a number is left-truncatable prime
def is_left_truncatable_prime(n):
    # Check if the number is less than 10
    if n < 10:
        # If it is, return False immediately since all numbers less than 10 are not left-truncatable prime numbers
        return False

    # Loop through all numbers from 2 to the number of digits in the number minus 1
    for i in range(2, len(str(n))) - 1):
        # Check if the leading digit is successively removed, then all resulting numbers are prime
        if is_prime(int(str(n)[i:])))
            return True

    # If none of the above conditions are met, return False since the number is not left-truncatable prime
    return False
