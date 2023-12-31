
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 54
    sum = 0
    for i in range(36, 54):
        if tuple[i] not in range(tuple[36], tuple[54])):
            sum += tuple[i]
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return "Binary representation string: {}".format(sum)
    else:
        return "Hexadecimal representation string: {}".format(sum)
