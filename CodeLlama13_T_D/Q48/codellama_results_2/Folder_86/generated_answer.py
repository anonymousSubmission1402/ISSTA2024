
def return_binary_or_hexa(arr):
    a = arr[19]
    b = arr[32]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in arr:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
