
def insert_before_character(string):
    return "".join([char if char != "j" else f"v{char}" for char in string])
