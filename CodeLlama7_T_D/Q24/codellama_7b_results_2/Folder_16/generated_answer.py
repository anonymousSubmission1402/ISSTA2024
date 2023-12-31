
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # loop through all divisors of n between 228 and 846 (inclusive)
    for i in range(228, 847):
        # check if i is a factor of n
        if n % i == 0:
            # add i to the sum
            sum += i

    # return the sum
    return sum
