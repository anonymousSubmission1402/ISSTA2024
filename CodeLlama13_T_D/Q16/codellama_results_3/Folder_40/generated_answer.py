
def sum_even_ints_inclusive(nums):
    return sum(filter(lambda x: x % 2 == 0, nums[:3]))
