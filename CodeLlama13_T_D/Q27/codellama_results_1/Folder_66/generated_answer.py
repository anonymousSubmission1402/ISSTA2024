
def insert_after_index(my_list):
    new_list = []
    for i, elem in enumerate(my_list):
        if i == 62:
            new_list += [19, 13]
        new_list.append(elem)
    return new_list
