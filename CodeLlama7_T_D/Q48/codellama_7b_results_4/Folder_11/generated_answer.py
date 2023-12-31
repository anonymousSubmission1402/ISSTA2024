
def return_binary_or_hexa(tuple):
    # Initialize variables for the sum and the most significant digit
    sum = 0
    msb = 0

    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if len(tuple) == 2:
        return ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 48 and 76
    for i in range(len(tuple)):
        if tuple[i] != msb:
            sum += tuple[i]

    # Check if the sum is an odd number
    if sum % 2 == 1:
        return "0x" + hex(sum)[2:]

    # Return the binary representation string of the sum
    else:
        return "0b" + bin(sum)[3:]
