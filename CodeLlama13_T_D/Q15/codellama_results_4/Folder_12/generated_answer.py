
def sum_odd_ints_inclusive(my_list):
    total = 0
    for i in range(14, 65):
        if my_list[i] % 2 != 0:
            total += my_list[i]
    return total
