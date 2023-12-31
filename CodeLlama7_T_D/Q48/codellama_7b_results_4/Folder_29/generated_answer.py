
def return_binary_or_hexa(tuple):
    # Get the integers stored at indices 70 and 98
    a = tuple[70]
    b = tuple[98]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 70 and 98
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[70:98]:
            sum += i
    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number
    if sum % 2 == 1:
        return "binary" + str(sum)
    else:
        return "hexadecimal" + str(sum)
