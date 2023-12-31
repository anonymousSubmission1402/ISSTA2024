
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 10 to index 100, both inclusive
    for i in range(10, 101):
        # If the current element is an even integer, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 10 to index 100, both inclusive
    return even_ints
