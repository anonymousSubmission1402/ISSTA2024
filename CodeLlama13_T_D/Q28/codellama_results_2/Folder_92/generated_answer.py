
def return_nth_smallest_ascii(s):
    char_count = {}
    for i in range(4):
        char = s[i]
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    min_ascii = None
    nth_smallest = None
    for char, count in char_count.items():
        ascii_value = ord(char)
        if min_ascii is None or ascii_value < min_ascii:
            min_ascii = ascii_value
            nth_smallest = char
    
    return nth_smallest
