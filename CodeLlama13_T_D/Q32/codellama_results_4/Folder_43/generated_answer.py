
def insert_after_character(s):
    return "".join([c + "G" if c == 't' else c for c in s])
