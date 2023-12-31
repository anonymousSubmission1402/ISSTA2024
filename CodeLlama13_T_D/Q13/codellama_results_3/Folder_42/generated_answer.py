
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    
    sorted_nums = sorted(nums)
    second_largest = sorted_nums[1]
    for i in range(2, len(sorted_nums)):
        if sorted_nums[i] != second_largest:
            break
    else:
        return None
    
    for i in range(29, 80):
        if nums[i] == second_largest:
            return second_largest
    return None
