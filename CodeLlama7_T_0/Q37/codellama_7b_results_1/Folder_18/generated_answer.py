
def filter_chars(string):
    filtered_string = ""
    for i in range(770, 971):
        if string[i] >= "-" and string[i] <= "D":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
