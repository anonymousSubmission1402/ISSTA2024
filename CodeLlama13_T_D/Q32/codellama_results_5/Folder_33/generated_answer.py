
def insert_after_character(string, character):
    return "".join([char if char != character else f"{character}n" for char in string])
