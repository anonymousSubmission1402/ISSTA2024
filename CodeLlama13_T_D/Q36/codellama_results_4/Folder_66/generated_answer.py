
def filter_chars(string):
    filtered = ""
    for char in string:
        if ord(char) > 39 and ord(char) < 87:
            filtered += char
        else:
            filtered += " "
    return filtered
