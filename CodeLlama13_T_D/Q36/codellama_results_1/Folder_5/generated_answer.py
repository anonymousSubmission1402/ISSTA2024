
def filter_chars(string):
    for i in range(55, 67):
        if string[i].isalpha() and string[i] > 'f' and string[i] < '|':
            string = string.replace(string[i], '')
    return string
