
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The input must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate through the divisors of n between 39 and 43 (both inclusive)
    for i in range(39, 44):
        if n % i == 0:
            sum += i

    # Return the sum
    return sum
