
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 23 <= i <= 89 and 'w' <= char <= '{':
            continue
        result += char
    return result
