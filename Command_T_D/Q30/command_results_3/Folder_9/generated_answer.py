import re
def insert_before_character(string):
    return re.sub(r'(e)', r'E\1', string)
