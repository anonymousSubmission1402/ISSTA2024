
def all_ints_not_div_by_num(my_list):
    divisible_indices = []
    for i in range(1, 7):
        if my_list[i] % 2 == 0:
            divisible_indices.append(i)
    return [my_list[i] for i in range(1, 7) if i not in divisible_indices]
