
def insert_before_character(s, char):
    return "".join("t" + c if c == char else c for c in s)
