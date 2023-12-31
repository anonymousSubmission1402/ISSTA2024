
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_divisors = 0

    # Iterate over the divisors of n in the specified range
    for i in range(372, 495):
        # Check if i is a divisor of n
        if n % i == 0:
            # Increment the sum of divisors by 1
            sum_divisors += 1

    # Return the sum of divisors
    return sum_divisors
