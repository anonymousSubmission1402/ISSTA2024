
def filter_chars(my_string):
    filtered_string = ""
    for i in range(58, 82):
        if my_string[i] > 'F' and my_string[i] < 'O':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
