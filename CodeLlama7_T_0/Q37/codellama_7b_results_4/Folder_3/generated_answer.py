
def filter_chars(string):
    filtered_string = ""
    for i in range(37, 56 + 1):
        char = string[i]
        if char >= "6" and char <= "_":
            continue

        filtered_string += char

    return filtered_string
