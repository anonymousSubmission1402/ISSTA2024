
def insert_after_character(string):
    return "".join([char if char != "O" else f"{char}O" for char in string])
