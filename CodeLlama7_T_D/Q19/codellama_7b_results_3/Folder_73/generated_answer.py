
def all_ints_not_div_by_num(my_list):
    divisible_integers = []
    for i in range(70, 98):
        if my_list[i] % -88 != 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
