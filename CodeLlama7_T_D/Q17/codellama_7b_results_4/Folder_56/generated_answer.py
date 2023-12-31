
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the list and check if each element is divisible by both -9 and -7
    for i in range(len(my_list)):
        if my_list[i] % (-9) == 0 and my_list[i] % (-7) == 0:
            # If the element is divisible by both numbers, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
