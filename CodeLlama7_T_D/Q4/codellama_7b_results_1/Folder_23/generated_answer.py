
def all_pos_ints_exclusive(my_list):
    # Find the starting index for positive integers
    start_index = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # Find the ending index for positive integers
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x > 0), None)
    # Return the list of all positive integers from start to end index, exclusive
    return my_list[start_index:end_index]
