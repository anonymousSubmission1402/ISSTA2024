
def return_binary_or_hexadecimal(numbers):
    a = numbers[22] + 1
    b = numbers[24] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in numbers:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
