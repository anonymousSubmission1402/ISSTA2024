
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 35 or i > 40:
            result += char
        elif char >= ")" and char <= "l":
            continue
        else:
            result += char
    return result
