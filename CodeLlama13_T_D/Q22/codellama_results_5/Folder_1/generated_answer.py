
def find_sum_of_multiples(num):
    return sum(i for i in range(1, 51 * num + 1) if i % num == 0)
