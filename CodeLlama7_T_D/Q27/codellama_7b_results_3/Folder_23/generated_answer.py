
def insert_after_index(my_list):
    # Find the index of the element after which we want to insert the new element
    idx = my_list.index(38) + 1
    # Insert the new element at the found index
    my_list.insert(idx, 45)
    return my_list
