
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if i == 9:
            new_list.insert(i + 1, 426.08)
    return new_list
