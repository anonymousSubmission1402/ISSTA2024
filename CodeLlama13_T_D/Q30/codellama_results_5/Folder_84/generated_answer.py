
def insert_before_character(string, char):
    return "".join([char if c == 'H' else c for c in string])
