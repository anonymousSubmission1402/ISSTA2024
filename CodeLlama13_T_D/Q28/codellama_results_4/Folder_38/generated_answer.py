
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[0:45]]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii_value = sorted_ascii_values[9]
    return chr(nth_smallest_ascii_value)
