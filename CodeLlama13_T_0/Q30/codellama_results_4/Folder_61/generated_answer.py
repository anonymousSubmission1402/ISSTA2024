
def insert_before_character(string):
    return "".join([char if char != "e" else "0" + char for char in string])
