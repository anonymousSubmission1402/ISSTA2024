
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(1, 67):
        if string[i-1] not in ascii_values:
            ascii_values.append(ord(string[i-1]))
    ascii_values.sort()
    return chr(ascii_values[7])
