
def filter_chars(string):
    filtered_string = ""
    for i in range(71, 96 + 1):
        char = string[i]
        if char >= "_" and char <= "o":
            continue

        filtered_string += char

    return filtered_string
