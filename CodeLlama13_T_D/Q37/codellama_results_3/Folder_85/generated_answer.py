
def filter_chars(string):
    return ''.join([char for char in string if not (28 <= ord(char) <= 65 and 'O' <= char <= 'd')])
