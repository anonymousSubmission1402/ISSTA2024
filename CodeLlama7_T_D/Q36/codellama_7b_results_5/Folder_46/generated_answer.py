
def filter_chars(string):
    filtered = ""
    for i in range(19, 69):
        if string[i] > '<' and string[i] < 'C':
            continue

        else:

            filtered += string[i]

    return filtered
