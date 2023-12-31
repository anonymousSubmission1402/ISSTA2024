
def return_binary_or_hexa(tuple):
    # Initialize variables for sum and range of indices
    sum = 0
    a = tuple[20]
    b = tuple[93]
    # Iterate over the range of indices
    for i in range(a + 1, b - 1):
        # Check if the current index is not present in the tuple between indices 20 and 93
        if i not in tuple[20:93]:
            # Add the current integer to the sum
            sum += i

    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
