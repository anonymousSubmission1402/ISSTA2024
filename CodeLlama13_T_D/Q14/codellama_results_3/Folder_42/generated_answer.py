
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)[21:97]
    second_smallest_num = sorted_list[1]
    return second_smallest_num
