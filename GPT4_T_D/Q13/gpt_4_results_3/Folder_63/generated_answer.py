
def find_second_largest_num(num_list):
    if len(num_list) < 23:
        return None
    else:
        sorted_num_list = sorted(num_list[22:89], reverse=True)
        if len(sorted_num_list) < 2:
            return None
        else:
            return sorted_num_list[1]
