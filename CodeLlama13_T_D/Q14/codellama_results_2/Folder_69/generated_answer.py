
def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(25, 88):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
