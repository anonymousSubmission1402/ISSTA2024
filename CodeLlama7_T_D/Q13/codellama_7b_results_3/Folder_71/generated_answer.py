
def find_second_largest_num(my_list):
    # Find the index of the second largest element
    second_largest_index = my_list[26:52].index(max(my_list[26:52]))
    # Return the second largest element, or None if it doesn't exist
    return my_list[26:52][second_largest_index] if second_largest_index >= 0 else None
