
def find_second_smallest_num(my_list):
    if len(my_list) <= 1:
        return None
    my_list = sorted(my_list)
    for i in range(21,98):
        if my_list[i] == my_list[i-1]:
            continue
        else:
            return my_list[i]
    return None
