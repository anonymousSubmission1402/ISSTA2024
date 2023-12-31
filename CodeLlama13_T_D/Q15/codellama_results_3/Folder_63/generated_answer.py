
def sum_odd_ints_inclusive(nums):
    # Slice the list to get the range of indices we want to include
    odd_nums = nums[22:89:2]
    
    # Sum the odd numbers in the slice using built-in sum() function
    return sum(odd_nums) if odd_nums else 0
