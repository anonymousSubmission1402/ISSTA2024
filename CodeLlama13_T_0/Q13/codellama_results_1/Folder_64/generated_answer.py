
def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest = sorted_list[4]
    for i in range(1, 5):
        if my_list[i] == second_largest:
            return None
    return second_largest
