
def insert_after_index(my_list):
    # Find the index of the element you want to insert after
    after_index = my_list.index(564) + 1
    # Insert the new element at the index found above
    my_list.insert(after_index, 149)
    return my_list
