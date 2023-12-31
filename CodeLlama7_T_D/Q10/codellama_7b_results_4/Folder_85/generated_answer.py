
def all_odd_ints_exclusive(my_list):
    odd_ints = []
    for i in range(4, 5 + 1): # Exclusive range of indices from 4 to 5
        if my_list[i] % 2 != 0: # If the integer at index i is odd
            odd_ints.append(my_list[i]) # Add the odd integer to the list
    return odd_ints # Return the list of all odd integers in the specified range
