
def return_n_greatest_chars(string):
    chars = set(string)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    greatest_chars = sorted_chars[-44:]
    return "".join(greatest_chars)
