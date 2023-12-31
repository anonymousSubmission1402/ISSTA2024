
def return_nth_smallest_ascii(string):
    char_count = {}
    for c in string:
        if ord(c) >= 17 and ord(c) <= 34:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
    
    sorted_chars = sorted(char_count, key=lambda x: (ord(x), -char_count[x]))
    return sorted_chars[17]
