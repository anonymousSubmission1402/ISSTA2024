
def filter_chars(string):
    filtered_string = ""
    for i in range(33, 70 + 1):
        if string[i] >= '7' and string[i] <= 'k':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
