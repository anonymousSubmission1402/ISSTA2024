
def filter_chars(s):
    result = ""
    for i in range(19, 34):
        if s[i].isalnum():
            result += s[i]
    return result
