
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting from index 29 and ending at index 93 (both inclusive)
    for i in range(29, 94):

        # Check if the current element is an even integer

        if my_list[i] % 2 == 0:

            # If it is, add it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers from index 29 to index 93 (both inclusive), or an empty list if no such integers exist in the specified range

    return even_ints
