
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if 42 <= ord(c) <= 59]
    ascii_values.sort()
    return chr(ascii_values[16])
