
def insert_after_character(string):
    return ''.join(f'w{c}' if c == 'r' else c for c in string)
