
def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 8 and nums[i] % 2 == 0:
            result += nums[i]
    return result
