
def if_perfect_num(numbers):
    return numbers[37] == sum(filter(lambda x: x % numbers[37] == 0, range(1, numbers[37])))
