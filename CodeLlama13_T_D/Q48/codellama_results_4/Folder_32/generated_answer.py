
def return_binary_or_hexa(nums):
    if nums[86] + 1 <= nums[90] - 1:
        sum = 0
        for i in range(nums[86] + 1, nums[90]):
            if not i in nums:
                sum += i
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]
    else:
        return ""
