
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list and append any even integers to the empty list
    for i in range(527, 538 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 527 to index 538, both inclusive
    return even_ints
