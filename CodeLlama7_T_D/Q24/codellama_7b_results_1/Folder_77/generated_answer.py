
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_of_divisors = 0

    # Iterate through the possible divisors of n
    for i in range(111, 508 + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add i to the sum of divisors
            sum_of_divisors += i

    # Return the sum of all positive divisors of n that are between 111 and 508, both inclusive
    return sum_of_divisors
