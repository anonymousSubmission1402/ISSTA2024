
def filter_chars(my_string):
    filtered_string = ""
    for i in range(58, 81):
        if my_string[i] > "5" and my_string[i] < ">":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
