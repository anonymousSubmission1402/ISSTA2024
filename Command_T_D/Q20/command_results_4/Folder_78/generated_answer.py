def find_n_th_smallest_num(nums):
    return sorted(set(nums))[nums.count(sorted(set(nums))[15]) - nums.count(sorted(set(nums))[70])]
