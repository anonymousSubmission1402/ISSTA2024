
def all_ints_not_div_by_num(my_list):
    # List slicing to get the required range of indices
    my_list = my_list[199:202]
    result = []
    for num in my_list:
        if num % -200 != 0:
            result.append(num)
    return result
