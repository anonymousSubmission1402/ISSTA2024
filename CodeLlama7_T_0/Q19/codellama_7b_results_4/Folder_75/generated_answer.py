
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(20, 51):
        if my_list[i] % -48 != 0:
            result.append(my_list[i])
    return result
