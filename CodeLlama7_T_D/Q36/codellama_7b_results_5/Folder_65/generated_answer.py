
def filter_chars(string):
    filtered_string = ""
    for i in range(58, 82):
        if string[i] > "F" and string[i] < "O":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
