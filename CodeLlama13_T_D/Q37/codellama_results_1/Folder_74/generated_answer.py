
def filter_chars(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isalpha() and 'f' <= s[i] <= 'o':
            new_str += s[i]
    return new_str
