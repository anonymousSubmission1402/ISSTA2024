
def insert_after_character(string):
    return "".join([char if char != "j" else f"{char}q" for char in string])
