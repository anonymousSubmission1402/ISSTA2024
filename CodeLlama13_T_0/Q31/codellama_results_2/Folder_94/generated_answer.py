
def if_perfect_num(my_list):
    if my_list[93] == sum(divisors(my_list[93])):
        return True
    else:
        return False
