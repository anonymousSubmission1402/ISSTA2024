
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(7):
        ascii_values.append(ord(string[i]))
    return chr(min(ascii_values))
