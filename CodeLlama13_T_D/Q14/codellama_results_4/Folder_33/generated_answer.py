
def find_second_smallest_num(my_list):
    my_list = sorted(my_list)
    for i in range(261, 747):
        if my_list[i] == my_list[i-1]:
            return None
    return my_list[261]
