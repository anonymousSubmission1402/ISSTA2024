
def insert_after_index(my_list):
    # Find the index of 42 in the list
    index_of_42 = my_list.index(42)
    # Insert 53 at the next index after 42
    new_list = my_list[:index_of_42 + 1] + [53] + my_list[index_of_42 + 1:]
    return new_list
