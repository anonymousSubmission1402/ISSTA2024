
def insert_before_character(string, char):
    return ''.join([f"q{char}" if c == "j" else c for c in string])
