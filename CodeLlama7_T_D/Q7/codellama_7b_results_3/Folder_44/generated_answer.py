
def all_even_ints_inclusive(my_list):
    # Get the range of even integers from index 13 to index 68, both inclusive
    even_int_range = [x for x in my_list[13:68+1] if x % 2 == 0]
    return even_int_range
