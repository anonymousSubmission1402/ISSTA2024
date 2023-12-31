
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 57
    end_index = 85
    div_by_77 = []
    div_by_32 = []

    # Iterate through the list and append integers divisible by -77 or -32 to respective lists
    for i in range(start_index, end_index + 1):
        if my_list[i] % -77 == 0:
            div_by_77.append(my_list[i])
        elif my_list[i] % -32 == 0:
            div_by_32.append(my_list[i])

    # Calculate sum of integers divisible by either -77 or -32
    div_by_either = div_by_77 + div_by_32
    sum = 0
    for i in div_by_either:
        sum += i

    # Return sum or 0 if no such integers exist in the specified range
    return sum if sum else 0
