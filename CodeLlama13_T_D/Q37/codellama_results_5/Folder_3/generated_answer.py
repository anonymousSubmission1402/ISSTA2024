
def filter_chars(string):
    filtered = ''
    for char in string:
        if 37 <= ord(char) <= 56 and '6' <= char <= '_':
            continue
        filtered += char
    return filtered
