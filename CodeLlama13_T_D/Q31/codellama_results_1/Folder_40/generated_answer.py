
def if_perfect_num(my_list):
    return my_list[7] == sum(filter(lambda x: x % my_list[7] == 0, range(1, int(my_list[7]) + 1)))
