
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[32:100] if x % -11 == 0 or x % -15 == 0])
