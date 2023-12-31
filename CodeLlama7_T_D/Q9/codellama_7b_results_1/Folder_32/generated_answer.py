
def all_odd_ints_inclusive(my_list):
    # Create an empty list to store the results
    result = []

    # Loop through the list from index 21 to index 97, both inclusive
    for i in range(21, 98):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the results list
            result.append(my_list[i])
    # Return the results list
    return result
