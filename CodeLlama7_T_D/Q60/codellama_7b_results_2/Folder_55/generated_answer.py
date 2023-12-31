
def all_left_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []
    # Loop through each integer in the tuple
    for i in range(len(tuple)):
        x = tuple[i]
        # Check if x is a prime number
        if is_prime(x):
            # Check if x is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(x):
                # Add x to the list of prime numbers
                prime_list.append(x)
    # Sort the list of prime numbers in descending order
    prime_list = sorted(prime_list, reverse=True)
    return prime_list

# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Convert the number to a string
    s = str(n)

    # Check if the number contains no 0
    if '0' not in s:
        # If the number contains no 0, check if it is a prime number
        if is_prime(n):
            # Loop through all the numbers from 2 to the square root of n
            for i in range(2, int(n ** 0.5) + 1)):
                # Check if i divides n
                if n % i == 0:
                    # If i divides n, return False
                    return False

            # If the number is a prime number and it is not divisible by any number between 2 and the square root of n, it is a left-and-right-truncatable prime number
            return True
