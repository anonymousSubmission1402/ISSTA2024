
def sum_odd_ints_inclusive(my_list):
    if len(my_list) <= 8:
        return 0
    else:
        return sum([x for x in my_list[8:9+1] if x % 2 != 0])
