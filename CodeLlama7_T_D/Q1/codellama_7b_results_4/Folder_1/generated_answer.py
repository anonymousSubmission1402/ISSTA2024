
def all_ints_inclusive(my_list):
    # Get the indices of the elements we want
    start_idx = 14
    end_idx = 64
    # Initialize an empty list to store the elements we want
    selected_elements = []

    # Iterate through the list and append the desired elements to the selected_elements list
    for i in range(start_idx, end_idx + 1):
        selected_elements.append(my_list[i])

    return selected_elements
