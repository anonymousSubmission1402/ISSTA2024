
def all_ints_div_by_num(my_list):
    result = []
    for i in range(255, 618 + 1):
        if my_list[i] % 965 == 0:
            result.append(my_list[i])
    return result
