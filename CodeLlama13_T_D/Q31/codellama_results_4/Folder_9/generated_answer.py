
def if_perfect_num(numbers):
    return numbers[24] == sum(filter(lambda x: x % numbers[24] == 0, range(1, numbers[24])))
