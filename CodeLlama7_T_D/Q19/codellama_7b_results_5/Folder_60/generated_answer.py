
def all_ints_not_div_by_num(my_list):
    # Create a new list to store the result
    result = []

    # Iterate through the input list and check if each element is not divisible by -99
    for i in my_list:
        if i % -99 != 0:
            result.append(i)

    # Return the resulting list
    return result
