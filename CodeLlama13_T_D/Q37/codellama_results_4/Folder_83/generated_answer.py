
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if 29 <= i <= 79 and 'K' <= c <= 'z':
            continue
        else:
            result += c
    return result
