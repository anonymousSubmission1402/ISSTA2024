
def if_perfect_num(nums):
    return nums[845] == sum(filter(lambda x: x % nums[845] == 0, range(1, nums[845])))
