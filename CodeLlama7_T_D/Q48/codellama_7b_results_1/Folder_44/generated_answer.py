
def return_binary_or_hexadecimal(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 52
    sum = 0
    for i in range(36, 52):
        if tuple[i] not in range(tuple[36], tuple[52] + 1)):
            sum += tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
