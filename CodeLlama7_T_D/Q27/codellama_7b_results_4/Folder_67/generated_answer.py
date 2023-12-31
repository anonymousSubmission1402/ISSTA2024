
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    # find the index where we want to insert the element
    insert_index = next((i for i, x in enumerate(my_list) if x == 44), None)
    # check if the element was found
    if insert_index is not None:
        # insert the element at the next index
        new_list.insert(insert_index + 1, 76)
    return new_list
