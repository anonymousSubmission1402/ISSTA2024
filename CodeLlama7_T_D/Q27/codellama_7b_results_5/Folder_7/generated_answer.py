
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index of the element following 323 in the list
    for i in range(len(new_list)):
        if new_list[i] == 323:
            new_list.insert(i + 1, [389, 303])
            break

    return new_list
