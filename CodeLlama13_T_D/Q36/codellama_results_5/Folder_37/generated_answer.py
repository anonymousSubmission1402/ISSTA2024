
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 44 <= ord(char) <= 59 and ord(char) > ord('/') < 6:
            continue
        result += char
    return result
