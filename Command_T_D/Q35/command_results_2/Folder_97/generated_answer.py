import re
def remove_repeat_chars(s):
    return re.sub(r"(\d)(?=\1)", r"1", s[34:69])
