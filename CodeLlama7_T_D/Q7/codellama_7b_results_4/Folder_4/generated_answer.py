
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers starting from index 12 to index 92, both inclusive
    for i in range(12, 93):

        # Check if the current integer is even and add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 12 to index 92, both inclusive
    return even_ints
