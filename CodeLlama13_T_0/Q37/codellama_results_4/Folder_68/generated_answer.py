
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 7 or i > 9:
            result += char
        elif char >= "6" and char <= "w":
            continue
        else:
            result += char
    return result
