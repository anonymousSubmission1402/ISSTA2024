
def return_nth_smallest_ascii(string):
    chars = set(string[0:5])
    asciis = sorted([ord(c) for c in chars])
    return chr(asciis[3])
