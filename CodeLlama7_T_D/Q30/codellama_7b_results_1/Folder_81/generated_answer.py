
def insert_before_character(string):
    return "".join([f"{c}" if c == "A" else f"{c}A" for c in string])
