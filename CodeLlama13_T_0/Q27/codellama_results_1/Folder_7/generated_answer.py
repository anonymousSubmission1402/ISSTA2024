
def insert_after_index(my_list):
    index = 323
    new_list = my_list[:index+1] + [389, 303] + my_list[index+1:]
    return new_list
