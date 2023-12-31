
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the specified range
    start = 56
    end = 98
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the input list
    for i in range(start, end + 1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of positive integers
    return pos_ints
