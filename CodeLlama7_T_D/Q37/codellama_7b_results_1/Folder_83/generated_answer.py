
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        if my_string[i].isalpha() and (ord(my_string[i]) >= ord('K') and ord(my_string[i]) <= ord('z')):
            continue

        filtered_string += my_string[i]
    return filtered_string
