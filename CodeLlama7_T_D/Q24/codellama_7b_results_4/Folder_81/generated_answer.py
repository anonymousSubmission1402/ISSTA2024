
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # initialize the sum to 0
    sum = 0
    # iterate through the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # if the current divisor is between 3 and 4 (inclusive), add it to the sum
        if n % i == 0 and i >= 3 and i <= 4:
            sum += i
    # return the sum of the divisors in the specified range
    return sum
