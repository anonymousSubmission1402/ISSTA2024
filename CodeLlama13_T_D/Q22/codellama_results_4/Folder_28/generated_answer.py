
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 43*n, n):
        sum += i
    return sum
