
def return_binary_or_hexa(my_tuple):
    a = my_tuple[36]
    b = my_tuple[54]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in my_tuple:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
