
def find_sum_of_multiples(n):
    if n <= 0:
        return 0

    multiples = []

    for i in range(1, 14):
        multiples.append(i * n)

    return sum(multiples)
