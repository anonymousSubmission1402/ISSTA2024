
def filter_chars(s):
    chars = list(s)
    for i in range(225, 381+1):
        if chars[i].isalpha() and 'D' <= chars[i] <= 'Y':
            chars[i] = ''
    return ''.join(chars)
