 def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if (char > "%") and (char < "a"):
            continue
        else:
            filtered_string += char
    return filtered_string
