import re
def insert_before_character(text):
    return re.sub(r'o', 'oo', text)
