
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].islower():
                if int(string[i]) >= 6 and int(string[i]) <= 10:
                    filtered_string += string[i]
            else:
                if int(string[i]) >= 6 and int(string[i]) <= 9:
                    filtered_string += string[i]
    return filtered_string
