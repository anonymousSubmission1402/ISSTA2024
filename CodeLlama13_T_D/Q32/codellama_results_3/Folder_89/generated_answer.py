
def insert_after_character(string):
    return "".join([char if char != "W" else "W W" for char in string])
