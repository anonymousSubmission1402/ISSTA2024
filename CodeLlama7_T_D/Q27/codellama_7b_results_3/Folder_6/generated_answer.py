
def insert_after_index(my_list):
    new_list = my_list[:] # Create a copy of the list
    index_to_insert = next((i for i, x in enumerate(my_list) if x == 581.49), None) # Find the index where we want to insert the value
    if index_to_insert is not None:
        new_list.insert(index_to_insert + 1, 581.49) # Insert the value at the next index after the one found
    return new_list
