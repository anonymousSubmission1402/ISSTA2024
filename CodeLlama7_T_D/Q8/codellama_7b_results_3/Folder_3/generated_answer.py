
def all_even_ints_exclusive(my_list):
    # Define the range of even integers
    start = 78
    end = 93
    # Initialize an empty list to store the result
    result = []
    # Iterate through the list and append each even integer to the result list
    for i in range(start, end):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
