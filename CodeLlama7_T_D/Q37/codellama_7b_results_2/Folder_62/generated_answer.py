
def filter_chars(string):
    filtered_string = ""
    for i in range(10, 69 + 1):
        char = string[i]
        if char >= "I" and char <= "K":
            continue
        else:
            filtered_string += char

    return filtered_string
