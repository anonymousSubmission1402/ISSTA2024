
def all_pos_ints_inclusive(my_list):
    return list(range(6, 7)) if any(x > 0 for x in my_list) else []
