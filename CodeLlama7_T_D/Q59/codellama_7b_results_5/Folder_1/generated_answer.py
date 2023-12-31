
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through each element in the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the element to the list of prime numbers
            prime_numbers.append(element)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If i divides n, return False
            if n % i == 0:
                return False

        # If we reach this point, then n is a prime number
        return True
