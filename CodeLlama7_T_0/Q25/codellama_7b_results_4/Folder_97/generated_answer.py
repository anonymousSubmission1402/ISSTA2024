
def insert_at_index(my_list):
    # Insert [912, 170] at index 500
    new_list = my_list[:500] + [912, 170] + my_list[500:]
    return new_list
