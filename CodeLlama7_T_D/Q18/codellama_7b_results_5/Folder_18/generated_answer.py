
def sum_ints_div_by_either_nums(my_list):
    start = 55
    end = 66
    divisible_ints = []

    for i in range(start, end + 1):
        if my_list[i] % 22 == 0 or my_list[i] % 82 == 0:
            divisible_ints.append(my_list[i])

    return sum(divisible_ints)
