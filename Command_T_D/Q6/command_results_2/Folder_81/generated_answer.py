def all_neg_ints_exclusive(nums):
    return [x for x in range(10, 100) if x in nums and x < 0]
