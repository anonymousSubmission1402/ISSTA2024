
def all_odd_ints_exclusive(my_list):
    # Check if the list is empty or has no odd integers in the specified range
    if len(my_list) == 0 or not any(i % 2 != 0 for i in my_list[276:376])):
        return []

    # Return the list of all odd integers from index 276 to index 376, both exclusive
    else:
        return [i for i in my_list[276:376] if i % 2 != 0]
