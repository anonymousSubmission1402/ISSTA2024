
def filter_chars(string):
    filtered_string = ""
    for i in range(318, 337):
        if string[i] > 'B' and string[i] < 'z':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
