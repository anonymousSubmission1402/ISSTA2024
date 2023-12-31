
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the list and check if each integer is not divisible by 36
    for i in range(10, 55):
        if my_list[i] % 36 != 0:
            # If the integer is not divisible by 36, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
