
def remove_repeat_chars(string):
    char_count = {}
    for i in range(69, 97):
        if string[i] not in char_count:
            char_count[string[i]] = 1
        else:
            char_count[string[i]] += 1
    
    for key in list(char_count.keys()):
        if char_count[key] > 1:
            string = string.replace(key, "")
    
    return string
