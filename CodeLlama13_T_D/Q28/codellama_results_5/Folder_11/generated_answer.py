
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[9:60]]
    return chr(sorted(ascii_values)[5])
