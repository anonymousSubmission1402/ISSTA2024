import re
def filter_chars(s):
    return re.sub(r'[A-Z][A-Z0-9_]{35}', '', s)
