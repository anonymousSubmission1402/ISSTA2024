
def insert_before_character(string):
    return "".join([char if char != "h" else "h5" for char in string])
