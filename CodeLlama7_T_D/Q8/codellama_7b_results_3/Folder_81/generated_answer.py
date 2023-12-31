
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list and check if each element is even
    for i in range(10, 100):
        if my_list[i] % 2 == 0:
            # If the element is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 10 to index 100, both exclusive
    return even_ints
