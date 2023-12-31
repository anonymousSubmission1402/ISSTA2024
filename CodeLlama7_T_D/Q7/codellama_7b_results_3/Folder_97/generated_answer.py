
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the specified range of the input list
    for i in range(40, 81):
        # Check if the current element is even and append it to the output list if so
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the output list
    return even_ints
