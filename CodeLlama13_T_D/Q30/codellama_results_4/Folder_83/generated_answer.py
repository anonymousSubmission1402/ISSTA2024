
def insert_before_character(string):
    return "".join([char if char != "E" else "e" + char for char in string])
