
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if i < 23 or i > 45:
            new_str += string[i]
        elif string[i] > "3" and string[i] < "I":
            new_str += string[i]
    return new_str
