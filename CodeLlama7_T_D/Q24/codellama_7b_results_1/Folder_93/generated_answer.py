
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate from 48 to 92, inclusive
    for i in range(48, 93):
        # Check if i is a divisor of n
        if n % i == 0:
            # Increment the sum by 1
            sum += 1

    # Return the sum
    return sum
