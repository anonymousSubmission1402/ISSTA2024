
def filter_chars(string):
    filtered = []
    for char in string:
        if char not in '()[]':
            filtered.append(char)
    return "".join(filtered)
