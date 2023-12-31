
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the specified range of the input list
    for i in range(50, 201):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the 'even_ints' list
            even_ints.append(my_list[i])

    return even_ints
