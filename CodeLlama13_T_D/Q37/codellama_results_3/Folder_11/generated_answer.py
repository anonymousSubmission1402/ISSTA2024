
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if 29 <= i < 97 and '-' <= c <= 'n':
            continue
        result += c
    return result
