
def all_ints_div_by_num(my_list):
    divisible_ints = []
    for i in range(57, 67 + 1):
        if my_list[i] % 90 == 0:
            divisible_ints.append(my_list[i])
    return divisible_ints
