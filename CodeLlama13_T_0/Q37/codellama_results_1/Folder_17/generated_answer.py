
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 27 or ord(char) > 29 or ord(char) < ord(';') or ord(char) > ord('b'):
            result += char
    return result
