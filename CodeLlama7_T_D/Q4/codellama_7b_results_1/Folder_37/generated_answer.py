
def all_pos_ints_exclusive(my_list):
    # Create an empty list to store the result
    result = []

    # Iterate through the list of integers
    for i in range(1, len(my_list)):
        # Check if the current element is positive
        if my_list[i] > 0:
            # Add the current element to the result list
            result.append(my_list[i])

    # Return the result list
    return result
