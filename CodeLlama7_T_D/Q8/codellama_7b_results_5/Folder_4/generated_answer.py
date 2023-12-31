
def all_even_ints_exclusive(my_list):
    # Find the first even integer index in the list
    for i in range(10, len(my_list), 2):
        if my_list[i] % 2 == 0:
            # Start looking for even integers from this index
            start_index = i
            break

    else:

        # No even integer found in the specified range

        return []

    # Find the last even integer index in the list

    for i in range(start_index, len(my_list), 2):
        if my_list[i] % 2 == 0:
            # End looking for even integers from this index

            end_index = i
            break

    else:

        # No even integer found in the specified range

        return []

    # Return a list of all even integers from the start index to the end index, exclusive

    return my_list[start_index:end_index]
