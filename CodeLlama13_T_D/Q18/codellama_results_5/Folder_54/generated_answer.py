
def sum_ints_div_by_either_nums(nums):
    return sum(x for i, x in enumerate(nums[13:92]) if i % -65 == 0 or i % -62 == 0)
