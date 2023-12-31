
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of integers
    for integer in tuple:
        # Check if the integer is a prime number
        if is_prime(integer):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(integer)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

# Check if an integer is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If it is, return False
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        # If it is divisible, return False
        if n % i == 0:
            return False

    # If none of the above conditions are true, return True
    return True
