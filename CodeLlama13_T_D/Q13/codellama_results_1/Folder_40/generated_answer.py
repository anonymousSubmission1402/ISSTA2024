
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    
    nums = sorted(nums)[-2:]
    
    if nums[0] == nums[1]:
        return None
    
    return nums[1]
