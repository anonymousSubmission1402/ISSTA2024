
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list from index 52 to index 53, both inclusive
    for i in range(52, 54):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    return prime_numbers

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

    return True
