
def insert_after_index(my_list):
    new_list = my_list[:]
    index_to_insert_at = my_list.index(693) + 1
    new_list.insert(index_to_insert_at, [606, 873])
    return new_list
