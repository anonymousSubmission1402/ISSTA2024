
def remove_repeat_chars(s):
    seen = set()
    new_string = ""
    for char in s:
        if char not in seen and len(seen) < 8:
            new_string += char
            seen.add(char)
    return new_string
