
def insert_after_index(my_list):
    index = 35
    new_list = my_list[:index+1] + [90, 76] + my_list[index+1:]
    return new_list
