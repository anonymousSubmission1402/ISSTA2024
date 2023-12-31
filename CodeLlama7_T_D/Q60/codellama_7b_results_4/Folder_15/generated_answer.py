
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by i
            if n % i == 0:
                # Return False if the number is not a prime number
                return False

    # Return True if the number is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize variables to store the digits of the number
    digits = []
    temp = n

    # Extract the digits of the number from the right side
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    # Check if the number is left-and-right-truncatable prime number
    for i in range(len(digits)):
        # Extract the digits from the left side and right side of the number
        left_digits = digits[:i]
        right_digits = digits[i:]

        # Check if the extracted digits form a prime number
        if is_prime(int(''.join(map(str, left_digits)))) and is_prime(int(''.join(map(str, right_digits)))):
            # Return True if the number is left-and-right-truncatable prime number
            return True
