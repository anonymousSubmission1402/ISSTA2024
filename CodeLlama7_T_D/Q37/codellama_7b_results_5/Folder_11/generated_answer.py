
def filter_chars(string):
    filtered_string = ""
    for i in range(29, 98):
        char = string[i]
        if char >= "-" and char <= "n":
            continue

        filtered_string += char

    return filtered_string
