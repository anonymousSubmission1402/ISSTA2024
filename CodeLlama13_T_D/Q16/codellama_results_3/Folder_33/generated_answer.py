
def sum_even_ints_inclusive(my_list):
    return sum(x for i, x in enumerate(my_list[667:775]) if i % 2 == 0)
