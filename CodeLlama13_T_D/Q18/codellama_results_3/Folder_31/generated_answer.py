
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(56, 89):
        if my_list[i] % -59 == 0 or my_list[i] % -79 == 0:
            result += my_list[i]
    return result
