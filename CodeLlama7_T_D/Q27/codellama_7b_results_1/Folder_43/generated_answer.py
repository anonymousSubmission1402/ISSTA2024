
def insert_after_index(my_list):
    # Find the index of the next element after 29
    next_element_index = my_list.index(29) + 1
    # Insert [28, 53] at the next element index
    my_list.insert(next_element_index, [28, 53])
    return my_list
