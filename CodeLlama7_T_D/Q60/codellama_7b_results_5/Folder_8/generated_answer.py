
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    
    # Iterate from 1 to x (inclusive)
    for i in range(1, x+1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If i is left-and-right-truncatable, add it to the list of prime numbers
                prime_list.append(i)
    
    # Sort the list of prime numbers in descending order
    prime_list.sort(reverse=True)
    
    # Return the list of prime numbers
    return prime_list

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False
    
    # Check if n is divisible by any integer between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False
    
    # If no factors were found, return True
    return True

# Define a function to check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False
    
    # Check if the leading leftmost and last rightmost digits of n are both prime numbers
    if is_prime(int(str(n)[0])) and is_prime(int(str(n)[-1])):
        return True
    
    # If the leading leftmost and last rightmost digits of n are not both prime numbers, return False
    return False
