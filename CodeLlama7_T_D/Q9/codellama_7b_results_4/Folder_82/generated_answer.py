
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the list
    first_odd = None
    for i in range(20, 201):
        if my_list[i] % 2 != 0:
            first_odd = my_list[i]
            break

    # If no odd integers exist in the specified range, return an empty list
    if first_odd is None:
        return []

    # Return the list of all odd integers from index 20 to index 200, both inclusive
    return [x for x in my_list[20:201] if x % 2 != 0]
