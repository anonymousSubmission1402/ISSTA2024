
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if (i < 55 or i > 66) and char != '|':
            result += char
    return result
