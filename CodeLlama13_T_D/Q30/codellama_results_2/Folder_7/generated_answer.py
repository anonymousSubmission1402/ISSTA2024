
def insert_before_character(s, c):
    return "".join([f"{c if x == ' ' else ''}{x}" for x in s])
