
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 23 < ord(char) < 83:
            continue

        else:

            filtered_string += char

    return filtered_string
