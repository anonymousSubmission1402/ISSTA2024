
import bisect

def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(34,81+1):
        if 27*i%57 == 0:
            result.append(i)
    return result
