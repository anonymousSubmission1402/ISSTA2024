
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        char = string[i]
        if (23 <= i <= 89) and ('w' <= char <= '{'):
            continue
        else:
            filtered_string += char

    return filtered_string
