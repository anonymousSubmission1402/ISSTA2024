
def find_second_smallest_num(num_list):
    try:
        sub_list = num_list[22:89]
        sub_list.sort()
        return sub_list[1]
    except IndexError:
        return None
