
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 2 or i > 3:
            result += char
        elif char >= "5" and char <= "_":
            continue
        else:
            result += char
    return result
