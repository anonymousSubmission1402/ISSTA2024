
def find_second_smallest_num(numbers):
    # Sort the list of numbers in ascending order
    sorted_nums = sorted(numbers)
    
    # Find the second smallest number between indices 70 and 200, both inclusive
    for i in range(70, 201):
        if sorted_nums[i] == sorted_nums[i-1]:
            continue
        else:
            return sorted_nums[i-1]
    
    # If there is no such element, return 'None'
    return None
