
def insert_after_character(string, char):
    return "".join([char + c if c == " " else c for c in string])
