def all_pos_ints_exclusive(nums):
    result = []
    for i in range(29, 53):
        if i in nums:
            result.append(i)
    return result
