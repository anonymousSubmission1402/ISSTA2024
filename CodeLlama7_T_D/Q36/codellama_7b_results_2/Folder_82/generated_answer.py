
def filter_chars(string):
    filtered_string = ""
    for i in range(69, 97):
        if string[i] > 'V' and string[i] < 'j':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
