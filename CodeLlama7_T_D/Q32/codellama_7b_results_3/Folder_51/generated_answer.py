
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "o":
            new_string += "O"
            if i + 1 < len(string) and string[i + 1] == "o":
                new_string += "o"
        else:
            new_string += string[i]
    return new_string
