
def all_right_truncatable_prime(tuple_of_positive_integers):
    # Initialize an empty list to store the sorted right-truncatable prime numbers less than x
    right_truncatable_prime_numbers = []
    # Get the integer at index 87 from the tuple of positive integers
    x = tuple_of_positive_integers[87]
    # Iterate over all prime numbers less than x
    for prime in range(2, x):
        # Check if the current prime number is right-truncatable by dividing it by its last rightmost digit and checking if the result is a prime number
        if is_prime(int(str(prime)[:-1])), prime % int(str(prime)[-1])):
            # If the current prime number is right-truncatable, add it to the list of right-truncatable prime numbers less than x
            right_truncatable_prime_numbers.append(prime)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(right_truncatable_prime_numbers)
# Check if a number is a prime number by iterating over its divisors and checking if any of them is other than 1 and the number itself
def is_prime(n):
    # Initialize an empty list to store the divisors of n
    divisors = []
    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if i is a divisor of n by dividing n by i and checking if the result is an integer
        if n % i == 0:
            # If i is a divisor of n, add it to the list of divisors
            divisors.append(i)
    # Return False if there are any divisors other than 1 and the number itself
    return len(divisors) == 2
