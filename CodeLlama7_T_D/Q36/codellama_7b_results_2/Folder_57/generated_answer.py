
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and string[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            filtered_string += string[i]
    return filtered_string
