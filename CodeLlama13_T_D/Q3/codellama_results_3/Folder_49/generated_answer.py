
def all_pos_ints_inclusive(my_list):
    result = []
    for i in range(80, 201):
        if my_list[i] > 0:
            result.append(my_list[i])
    return result
