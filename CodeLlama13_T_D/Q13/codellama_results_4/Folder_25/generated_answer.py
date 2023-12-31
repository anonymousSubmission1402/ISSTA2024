
def find_second_largest_num(my_list):
    # Find the second largest element in the list
    second_largest = sorted(my_list)[29:94]
    
    # If there is no such element, return None
    if not second_largest:
        return None
    
    # Otherwise, return the second largest element
    return second_largest[-1]
