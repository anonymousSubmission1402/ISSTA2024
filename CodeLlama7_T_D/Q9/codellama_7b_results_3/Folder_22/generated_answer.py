
def all_odd_ints_inclusive(my_list):
    # Get the starting and ending indices of the range
    start = max(40, my_list.index(next((x for x in my_list if x % 2 == 1), None))))
    end = min(200, my_list.index(next((x for x in my_list[start:] if x % 2 == 1), None)))))

    # Return the list of all odd integers within the specified range
    return [x for x in my_list[start:end+1] if x % 2 == 1]
