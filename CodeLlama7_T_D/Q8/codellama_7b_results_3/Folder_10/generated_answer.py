
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the range
    for i in range(48, 75):
        if my_list[i] % 2 == 0:
            first_even = i
            break

    else:

        return []


    # Create a list of all even integers in the range

    even_ints = []

    for i in range(first_even, len(my_list)):

        if my_list[i] % 2 == 0:

            even_ints.append(my_list[i])


    return even_ints
