
def filter_chars(string):
    filtered_string = ''
    for i in range(36, 80):
        char = string[i]
        if char >= 'a' and char <= 'i':
            continue

        filtered_string += char

    return filtered_string
