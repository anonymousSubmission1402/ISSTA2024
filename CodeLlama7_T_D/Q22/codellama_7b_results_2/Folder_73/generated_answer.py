
def find_sum_of_multiples(n):
    if n < 1:
        return 0

    sum = 0

    for i in range(19):

        sum += n * (i + 1)

    return sum
