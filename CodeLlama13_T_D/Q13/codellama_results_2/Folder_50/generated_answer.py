
def find_second_largest_num(distinct_nums):
    if len(distinct_nums) <= 84:
        return None
    second_largest = distinct_nums[79]
    for i in range(80, len(distinct_nums)):
        if distinct_nums[i] > second_largest:
            second_largest = distinct_nums[i]
    return second_largest
