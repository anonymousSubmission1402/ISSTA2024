
def filter_chars(string):
    filtered_string = ""
    for i in range(36, 80):
        if string[i] >= "2" and string[i] <= "s":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
