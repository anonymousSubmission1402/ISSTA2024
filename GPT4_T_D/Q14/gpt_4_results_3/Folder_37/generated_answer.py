
def find_second_smallest_num(num_list):
    if len(num_list) < 8:
        return None
    else:
        sublist = num_list[5:8]
        sublist.sort()
        return sublist[1]
