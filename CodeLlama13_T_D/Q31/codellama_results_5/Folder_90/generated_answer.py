
def if_perfect_num(numbers):
    return numbers[263] == sum(filter(lambda x: x % numbers[263] == 0, range(1, numbers[263])))
