
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(13, 76):
        if my_list[i] % 44 != 0:
            result.append(my_list[i])
    return result
