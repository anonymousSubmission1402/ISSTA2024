
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    if len(sorted_list) <= 71:
        return None
    else:
        return sorted_list[52:72]
