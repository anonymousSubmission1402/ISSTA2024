
def filter_chars(string):
    return "".join([char for char in string if not (5 <= ord(char) <= 6 and 'G' <= char <= 'p')])
