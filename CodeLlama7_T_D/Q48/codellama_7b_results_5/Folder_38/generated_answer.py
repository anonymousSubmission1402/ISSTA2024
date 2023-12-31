
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 85.
    sum = 0
    for i in range(36, 85 + 1):
        if my_tuple[i] != my_tuple[36] + i - 35:
            sum += my_tuple[36] + i - 35
    # Return the binary or hexadecimal representation string of the sum.
    if sum % 2 == 0:
        return "{:X}".format(sum)
    else:
        return "{:b}".format(sum)
