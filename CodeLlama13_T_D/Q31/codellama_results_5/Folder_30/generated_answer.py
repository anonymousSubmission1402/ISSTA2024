
def if_perfect_num(numbers):
    return numbers[94] == sum(set([i for i in range(1, int(numbers[94])**0.5+1) if numbers[94] % i == 0]))
