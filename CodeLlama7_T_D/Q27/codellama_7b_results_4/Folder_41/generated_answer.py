
def insert_after_index(my_list):
    new_list = my_list[:]
    index = my_list.index(78, 16) + 1
    new_list.insert(index, 78, 16)
    return new_list
