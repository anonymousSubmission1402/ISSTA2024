
def insert_at_index(my_list):
    # Create a new list with one more element than the original list
    new_list = my_list[:84] + [13, 46] + my_list[84:]
    return new_list
