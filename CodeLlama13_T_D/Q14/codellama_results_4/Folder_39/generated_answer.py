
def find_second_smallest_num(nums):
    nums = sorted(nums)
    for i in range(28, 41):
        if i == len(nums)-1:
            return None
        if nums[i] != nums[i-1]:
            return nums[i]
    return None
