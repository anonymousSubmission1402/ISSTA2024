
def insert_after_character(s):
    return "".join([char if char != "m" else f"{char}N" for char in s])
