
def all_ints_div_by_num(my_list):
    # Find the first index where the condition is not met
    first_index = next((i for i, x in enumerate(my_list) if x % -57 != 0), len(my_list))
    # Find the last index where the condition is not met
    last_index = next((i for i in range(first_index, len(my_list)) if my_list[i] % -57 != 0)), None)
    # Return the list of integers divisible by -57 from the specified range
    return [x for x in my_list[first_index:last_index+1] if x % -57 == 0]
