
def insert_after_character(string):
    return "".join([char if char != "Q" else "Q" for char in string])
