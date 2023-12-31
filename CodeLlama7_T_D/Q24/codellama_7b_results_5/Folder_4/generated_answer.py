
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # Check if the divisor is between 48 and 60
            if 48 <= i <= 60:
                sum += i

    return sum
