
def remove_repeat_chars(s):
    # Create a dictionary to store the characters and their counts
    char_count = {}
    for i in range(56, 88):
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1
    
    # Remove all occurrences of repeated characters from the string
    for i in range(56, 88):
        if s[i] in char_count and char_count[s[i]] > 1:
            s = s.replace(s[i], "")
    
    return s
