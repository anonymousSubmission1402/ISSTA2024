
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(13, 19):
        if my_list[i] % 45 == 0 or my_list[i] % 20 == 0:
            result += my_list[i]
    return result
