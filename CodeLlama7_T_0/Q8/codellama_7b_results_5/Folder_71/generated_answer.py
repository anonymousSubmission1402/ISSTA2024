
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers, starting from index 36 and ending at index 54 (both exclusive)
    for i in range(36, 54):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range, or an empty list if no such integers exist
    return even_ints
