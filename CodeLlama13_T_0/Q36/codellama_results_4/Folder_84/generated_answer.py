
def filter_chars(string):
    new_str = ""
    for i in range(171, 636):
        if string[i] > "c" and string[i] < "s":
            new_str += string[i]
    return new_str
