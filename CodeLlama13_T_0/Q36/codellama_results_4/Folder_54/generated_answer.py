
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 18 or i > 38:
            new_str += char
        elif char > ")" and char < "P":
            new_str += char
    return new_str
