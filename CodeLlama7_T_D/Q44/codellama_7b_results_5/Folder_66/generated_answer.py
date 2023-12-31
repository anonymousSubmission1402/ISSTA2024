
def composite_nums_between_indices(my_list):
    # Check if the input list is valid
    if not my_list or len(my_list) < 62:
        return set()
    # Find the indices of the first and last composite numbers in the list
    first_composite = None
    last_composite = None
    for i in range(len(my_list)):
        if my_list[i] > 1 and is_prime(my_list[i])):
            first_composite = i
            break

    for i in range(len(my_list) - 1, -1, -1)):
        if my_list[i] > 1 and is_prime(my_list[i])):
            last_composite = i
            break

    # Return the set of all composite numbers in the specified range
    return set([my_list[i] for i in range(first_composite, last_composite + 1)]))
