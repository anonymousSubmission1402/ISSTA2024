
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "A":
            new_string += "A"
            new_string += string[i]
        else:
            new_string += string[i]
    return new_string
