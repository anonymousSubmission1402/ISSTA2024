
def filter_chars(string):
    result = ""
    for i in range(155, 403+1):
        if string[i].isalpha():
            result += string[i]
    return result
