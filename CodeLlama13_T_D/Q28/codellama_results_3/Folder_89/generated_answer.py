
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[24:71]]
    nth_smallest_ascii = sorted(ascii_values)[7]
    return chr(nth_smallest_ascii)
