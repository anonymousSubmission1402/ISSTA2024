
def insert_after_character(string):
    return "".join([c + ("d" if c == "O" else "") for c in string])
