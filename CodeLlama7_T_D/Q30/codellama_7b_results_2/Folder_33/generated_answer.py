
def insert_before_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "n":
            result += "n"
        if char == "a":
            result += "an"
        else:
            result += char

    return result
