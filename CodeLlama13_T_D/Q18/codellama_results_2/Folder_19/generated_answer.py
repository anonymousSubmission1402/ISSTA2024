
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(1, 4):
        if my_list[i] % -6 == 0 or my_list[i] % 4 == 0:
            result += my_list[i]
    return result
