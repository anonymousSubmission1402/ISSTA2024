
def if_perfect_num(my_list):
    return my_list[15] == sum(divisors(my_list[15])) - my_list[15]
