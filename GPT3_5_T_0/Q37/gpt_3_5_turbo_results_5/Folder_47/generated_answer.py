
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 38 or i > 54 or char < ':' or char > 'r'])
