
def filter_chars(string):
    for i in range(25, 97+1):
        char = string[i]
        if 'm' <= char <= 'w':
            string = string.replace(char, '')
    return string
