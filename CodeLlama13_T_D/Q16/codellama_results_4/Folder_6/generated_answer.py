
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list) if 10 <= i <= 66 and x % 2 == 0)
