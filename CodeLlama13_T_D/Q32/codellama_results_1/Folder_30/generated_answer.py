
def insert_after_character(string):
    return "".join([char if char != "F" else "F4" for char in string])
