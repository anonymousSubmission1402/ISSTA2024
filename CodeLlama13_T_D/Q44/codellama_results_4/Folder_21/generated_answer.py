
def composite_nums_between_indices(my_list):
    # Find the indices of the start and end points of the specified range
    start_index = my_list.index(262)
    end_index = my_list.index(746)
    
    # Return the set of all composite numbers in the given list that are between index 262 to index 746, both inclusive
    return {num for num in my_list[start_index:end_index+1] if num > 1 and not isinstance(num, int)}
