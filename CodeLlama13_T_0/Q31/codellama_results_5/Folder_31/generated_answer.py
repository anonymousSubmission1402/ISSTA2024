
def if_perfect_num(my_list):
    if my_list[66] == sum(my_list[:my_list[66]]) and all(my_list[:my_list[66]]):
        return True
    else:
        return False
