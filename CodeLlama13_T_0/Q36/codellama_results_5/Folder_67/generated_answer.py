
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 18 or i > 31:
            result += char
        elif char > "H" and char < "|":
            continue
        else:
            result += char
    return result
