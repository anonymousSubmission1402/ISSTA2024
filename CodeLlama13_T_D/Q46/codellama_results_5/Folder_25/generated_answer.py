
def gcf_three_nums(nums):
    return _gcf(nums[32], nums[54], nums[13])

def _gcf(a, b, c):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
