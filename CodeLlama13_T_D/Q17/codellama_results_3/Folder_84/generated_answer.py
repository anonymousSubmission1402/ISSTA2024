
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(78, 82):
        if my_list[i] % 76 == 0 and my_list[i] % 60 == 0:
            result.append(my_list[i])
    return result
