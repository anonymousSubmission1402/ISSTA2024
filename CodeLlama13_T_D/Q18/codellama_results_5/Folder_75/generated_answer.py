
def sum_ints_div_by_either_nums(my_list):
    return sum(x for x in my_list[20:94] if (x % -92 == 0) or (x % -50 == 0))
