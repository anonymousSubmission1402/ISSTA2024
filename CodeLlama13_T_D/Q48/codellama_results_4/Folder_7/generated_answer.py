
def return_binary_or_hexa(numbers):
    a = numbers[10] + 1
    b = numbers[97] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in numbers:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
