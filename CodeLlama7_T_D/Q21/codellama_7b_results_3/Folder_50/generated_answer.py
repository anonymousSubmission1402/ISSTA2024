
def all_ints_div_by_num(my_list):
    # Find the first index where the integer is divisible by 28
    start_index = next((i for i, x in enumerate(my_list) if x % 28 == 0), None)
    # If no such integer exists, return an empty list
    if start_index is None:
        return []

    # Find the last index where the integer is divisible by 28
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 28 == 0), None)
    # If no such integer exists, return an empty list
    if end_index is None:
        return []

    # Return the list of all integers divisible by 28 from index 36 to index 46, both inclusive
    return my_list[start_index + 36 : end_index + 46]
