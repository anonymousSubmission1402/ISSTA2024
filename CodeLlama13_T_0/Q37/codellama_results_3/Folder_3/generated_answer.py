
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 37 or i > 56:
            result += char
        elif char >= "6" and char <= "_":
            continue
        else:
            result += char
    return result
