
def all_right_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_truncatable_primes = []

    # Loop through each integer in the tuple

    for integer in tuple_of_integers:

        # If the integer is a prime number, add it to the list of right-truncatable prime numbers

        if is_prime(integer):

            right_truncatable_primes.append(integer)

    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):

    # If n is less than 2, it is not a prime number

    if n < 2:

        return False


    # Check if n is divisible by any number between 2 and the square root of n

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
