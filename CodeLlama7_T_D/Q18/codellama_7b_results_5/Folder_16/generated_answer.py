
def sum_ints_div_by_either_nums(my_list):
    start = 55
    end = 80
    result = 0
    for i in range(start, end + 1):
        if my_list[i] % 22 == 0 or my_list[i] % 32 == 0:
            result += my_list[i]
    return result
