
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    index = my_list.index(323) + 1 # find the index of 323 and add 1 to it
    new_list.insert(index, [389, 303]) # insert [389, 303] at the found index
    return new_list
