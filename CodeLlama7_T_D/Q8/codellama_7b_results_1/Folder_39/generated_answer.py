
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(43, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    # Find the last even integer in the list

    for j in range(start, len(my_list)):
        if my_list[j] % 2 == 0:
            end = j
            break

    # Return the list of all even integers between start and end

    return [my_list[k] for k in range(start + 1, end)]
