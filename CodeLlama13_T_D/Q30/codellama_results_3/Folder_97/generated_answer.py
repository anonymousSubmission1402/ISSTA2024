
def insert_before_character(string):
    return "".join([f"h{c}" if c == 'o' else c for c in string])
