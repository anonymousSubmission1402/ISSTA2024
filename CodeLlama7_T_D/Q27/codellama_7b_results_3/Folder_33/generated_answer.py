
def insert_after_index(my_list):
    new_list = my_list[:] # Create a shallow copy of the list
    index_to_insert = my_list.index(974.0, 556) + 1 # Find the index where we want to insert the element
    new_list.insert(index_to_insert, 974.0) # Insert the element at the found index
    return new_list
