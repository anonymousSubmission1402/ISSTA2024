
def filter_chars(string):
    filtered_string = ""
    for i in range(38, 69 + 1):
        if string[i] >= "H" and string[i] <= "e":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
