 def filter_chars(string):
    for i in range(669, 888):
        if string[i] > 'B' and string[i] < 'Y':
            string = string[:i] + string[i+1:]
    return string
