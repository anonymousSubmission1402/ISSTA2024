
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if char >= 'R' and char <= 't':
            continue

        filtered_string += char

    return filtered_string
