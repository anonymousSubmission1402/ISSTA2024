
def all_left_truncatable_prime(tuple):
    # Initialize list of prime numbers
    prime_numbers = []

    # Loop through the tuple
    for i in range(len(tuple)):
        # Get the current number
        num = tuple[i]

        # Check if the number is prime
        if is_prime(num):
            # Add the prime number to the list
            prime_numbers.append(num)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers


def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
