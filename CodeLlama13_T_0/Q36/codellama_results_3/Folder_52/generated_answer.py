
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 49 or i > 56:
            new_str += char
        elif char > "I" and char < "a":
            new_str += char
    return new_str
