
def if_perfect_num(my_list):
    if my_list[97] == sum(filter(lambda x: x % my_list[97] == 0, range(1, my_list[97]))):
        return True
    else:
        return False
