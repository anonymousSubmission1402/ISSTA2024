
def if_perfect_num(my_list):
    if my_list[53] == sum(divisors(my_list[53])):
        return True
    else:
        return False
