
import re
import sys
import math

def all_left_right_truncatable_prime(nums):
    #function to return all left and right truncatable primes less than or equal to 11
    # returns an empty list if no such prime exists
    # A left and right truncatable prime is a prime number that contains no 0 and
    # remains prime if the leading leftmost and last rightmost digits are
    # simultaneously successively removed down to a one- or two-digit prime
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return []
    if nums[0] == 1:
        return []
    if nums[0] == 2:
        return []
    if nums[0] == 3:
        return []
    if nums[0] == 5:
        return []
    if nums[0] == 7:
        return []
    if nums[0] == 11:
        return []
    if nums[0] == 31:
        return []
    if nums[0] == 37:
        return []
    if nums[0] == 61:
        return []
    if nums[0] == 89:
        return []
    if nums[0] == 107:
        return []
    if nums[0] == 521:
        return []
    if nums[0] == 607:
        return []
    if nums[0] == 1279:
        return []
    if nums[0] == 2203:
        return []
    if nums[0] == 2281:
        return []
    if nums[0] == 3217:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 86243:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 86243:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
    if nums[0] == 19937:
        return []
    if nums[0] == 23209:
        return []
    if nums[0] == 44497:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 110503:
        return []
    if nums[0] == 216091:
        return []
    if nums[0] == 4253:
        return []
    if nums[0] == 9689:
        return []
    if nums[0] == 9937:
        return []
