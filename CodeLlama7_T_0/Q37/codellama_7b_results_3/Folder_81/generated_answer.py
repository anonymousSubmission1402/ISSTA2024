
def filter_chars(string):
    filtered_string = ""
    for i in range(19, 93):
        char = string[i]
        if char >= "8" and char <= "m":
            continue

        filtered_string += char

    return filtered_string
