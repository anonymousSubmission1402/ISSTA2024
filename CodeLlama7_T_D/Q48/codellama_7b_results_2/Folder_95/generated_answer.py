
def return_binary_or_hexa(tuple):
    # Get the elements between indices 32 and 99
    elements = tuple[32:99]
    # Initialize the sum to 0
    sum = 0
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 32 and 99
    for i in range(tuple[32] + 1, tuple[99] - 1):
        if i not in elements:
            sum += i

    # Check if the sum is an odd number

    if sum % 2 == 1:

        # Return the binary representation string of the sum

        return bin(sum)[2:]

    else:

        # Return the hexadecimal representation string of the sum

        return hex(sum)[2:]
