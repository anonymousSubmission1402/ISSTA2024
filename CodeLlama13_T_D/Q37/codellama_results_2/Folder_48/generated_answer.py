
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if not (513 <= i < 877 and '?' <= char <= 'n'):
            result += char
    return result
