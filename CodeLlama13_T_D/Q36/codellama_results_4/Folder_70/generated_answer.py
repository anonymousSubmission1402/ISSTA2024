
def filter_chars(s):
    new_string = ''
    for i, char in enumerate(s):
        if (170 <= i < 195) and (char > '!' and char < '}'):
            new_string += s.replace(char, '')
        else:
            new_string += char
    return new_string
