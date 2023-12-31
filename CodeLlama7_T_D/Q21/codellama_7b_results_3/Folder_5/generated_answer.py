 def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_list = []
    # Iterate over the specified range of indices in the input list
    for i in range(1, len(my_list)):
        # Check if the current element is divisible by -6
        if my_list[i] % -6 == 0:
            # If it is, add it to the list of divisible integers
            div_list.append(my_list[i])
    # Return the list of all divisible integers in the specified range
    return div_list
