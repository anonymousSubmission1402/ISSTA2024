
def all_even_ints_inclusive(nums):
    result = []
    for i in range(36, 46):
        if i % 2 == 0:
            result.append(nums[i])
    return result
