import re
def filter_chars(str):
    return re.sub(r'[A-Z][^G-J]', '', str)
