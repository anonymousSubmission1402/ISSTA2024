
def insert_after_index(my_list):
    new_list = my_list[:] # create a copy of the list
    for i in range(len(my_list)):
        if i == 1: # if the current index is 1, insert 478.12 at the next index
            new_list.insert(i+1, 478.12)
    return new_list
