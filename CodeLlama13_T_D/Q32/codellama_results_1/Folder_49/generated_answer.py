
def insert_after_character(string):
    return "".join([char + "i" if char == "i" else char for char in string])
