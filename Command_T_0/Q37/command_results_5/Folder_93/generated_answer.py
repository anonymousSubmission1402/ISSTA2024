import re
def filter_chars(s):
    return re.sub(r'[A-E][^H-e]', '', s)
