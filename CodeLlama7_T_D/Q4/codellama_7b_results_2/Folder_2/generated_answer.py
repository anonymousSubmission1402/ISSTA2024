
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer index in the list
    for i, x in enumerate(my_list):
        if x > 0:
            break

    # Find the last positive integer index in the list

    for j, y in enumerate(my_list[::-1]):
        if y > 0:
            break

    # Return the list of all positive integers from the specified range

    return my_list[i+36:j+52]
