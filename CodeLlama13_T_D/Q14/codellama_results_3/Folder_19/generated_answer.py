
def find_second_smallest_num(my_list):
    if len(my_list) <= 8:
        return None
    sorted_list = sorted(my_list[4:9])
    for i in range(4, 8):
        if my_list[i] == sorted_list[1]:
            return my_list[i]
    return None
