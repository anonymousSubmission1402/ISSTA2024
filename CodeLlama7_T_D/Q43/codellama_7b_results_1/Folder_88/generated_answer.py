
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through the list and check if each element is a prime number
    for i in range(10, len(my_list)):
        if is_prime(my_list[i]):
            # If the element is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any of the numbers in the range, it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any of the numbers in the range, it is prime
    return True
