
def filter_chars(string):
    new_str = ""
    for i in range(299, 418):
        if string[i].isdigit() and string[i] > '9' and string[i] < 'P':
            new_str += string.replace(string[i], "")
        else:
            new_str += string[i]
    return new_str
