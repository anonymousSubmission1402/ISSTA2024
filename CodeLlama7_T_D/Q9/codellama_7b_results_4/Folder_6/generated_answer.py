
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the range
    first_odd = next((i for i in my_list[10:66+1] if i % 2), None)
    # If no odd integers exist in the range, return an empty list
    if first_odd is None:
        return []

    # Return the list of all odd integers from index 10 to index 66, both inclusive
    return [i for i in my_list[10:66+1] if i % 2]
