 def filter_chars(s):
    start = 515
    end = 538
    filtered_string = ""
    for i in range(start, end + 1):
        if s[i].isalpha():
            continue

        else:

            filtered_string += s[i]

    return filtered_string
