
def insert_after_character(string, char):
    new_string = ""
    for i in range(len(string)):
        if string[i] == char:
            new_string += string[:i+1] + "k" + string[i+1:]
        else:
            new_string += string[i]
    return new_string
