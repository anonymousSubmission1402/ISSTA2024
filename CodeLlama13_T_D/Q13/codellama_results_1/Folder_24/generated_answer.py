
def find_second_largest_num(my_list):
    if len(my_list) <= 1:
        return None

    sorted_list = sorted(my_list)
    second_largest = sorted_list[-2]

    for i in range(74, 96):
        if my_list[i] == second_largest:
            return second_largest

    return None
