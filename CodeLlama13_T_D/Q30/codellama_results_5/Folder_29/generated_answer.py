
def insert_before_character(string):
    return "".join([f"z{c}" if c == "N" else f"{c}" for c in string])
