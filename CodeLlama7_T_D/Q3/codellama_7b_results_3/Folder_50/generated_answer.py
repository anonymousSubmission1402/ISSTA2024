
def all_pos_ints_inclusive(my_list):
    start = 70
    end = 84
    pos_ints = []
    for i in range(start, end + 1):
        if my_list[i - 1] > 0:
            pos_ints.append(my_list[i - 1])
    return pos_ints
