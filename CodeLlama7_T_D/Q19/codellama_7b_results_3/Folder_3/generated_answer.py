
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the specified range of indices in the input list
    for i in range(31, 70):

        # Check if the current element is not divisible by -70
        if my_list[i] % -70 != 0:

            # If the condition is true, add the current element to the result list
            result.append(my_list[i])

    # Return the result list
    return result
