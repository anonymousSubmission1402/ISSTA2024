
def find_second_smallest_num(my_list):
    return sorted(set(my_list[30:87]))[1] if len(set(my_list[30:87])) > 1 else None
