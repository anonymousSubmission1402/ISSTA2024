
def insert_after_index(my_list):
    new_list = my_list[:]
    index = my_list.index(717.02, 28) + 1
    new_list.insert(index, 717.02)
    return new_list
