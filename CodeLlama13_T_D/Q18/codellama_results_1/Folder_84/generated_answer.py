
def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(78, 82):
        if numbers[i] % 76 == 0 or numbers[i] % 60 == 0:
            total += numbers[i]
    return total
