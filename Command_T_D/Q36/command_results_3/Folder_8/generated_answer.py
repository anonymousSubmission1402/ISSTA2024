import re
def filter_chars(s):
    return re.sub(r'([A-Z])([^A-Z]*)', r'\1\2', s)
