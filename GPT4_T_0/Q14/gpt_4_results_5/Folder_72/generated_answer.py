
def find_second_smallest_num(num_list):
    if len(num_list) < 87:
        return None
    else:
        sub_list = num_list[82:87]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[1]
