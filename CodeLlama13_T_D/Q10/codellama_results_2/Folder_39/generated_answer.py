
def all_odd_ints_exclusive(my_list):
    return [x for x in my_list if 43 <= my_list.index(x) < 99 and x % 2 == 1]
