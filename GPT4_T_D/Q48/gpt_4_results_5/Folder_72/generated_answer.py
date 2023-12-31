
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_nums = set(range(a + 1, b)) - set(numbers[13:71])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]
