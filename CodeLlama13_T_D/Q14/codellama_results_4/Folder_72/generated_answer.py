
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    my_list.sort()
    second_smallest = my_list[1]
    for i in range(82, 86 + 1):
        if my_list[i] == second_smallest:
            return my_list[i]
    return None
