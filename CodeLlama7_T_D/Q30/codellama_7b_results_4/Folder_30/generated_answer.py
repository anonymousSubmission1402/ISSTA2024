
def insert_before_character(string, character):
    result = ""
    for i in range(len(string)):
        if string[i] == character:
            result += string[:i] + "F" + string[i:]
            break

    return result
