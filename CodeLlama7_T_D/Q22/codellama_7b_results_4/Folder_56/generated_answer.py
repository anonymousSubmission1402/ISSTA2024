
def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    sum = 0

    for i in range(64):

        sum += (i + 1) * n

    return sum
