
def filter_chars(my_string):
    filtered_string = ""
    for i in range(15, len(my_string)):
        if my_string[i] > "I" and my_string[i] < "M":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
