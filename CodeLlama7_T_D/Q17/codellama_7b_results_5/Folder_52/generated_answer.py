
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate over the list and check if each integer is divisible by both 88 and 58
    for i in range(48, 60):
        if my_list[i] % 88 == 0 and my_list[i] % 58 == 0:
            # If the integer is divisible by both 88 and 58, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
