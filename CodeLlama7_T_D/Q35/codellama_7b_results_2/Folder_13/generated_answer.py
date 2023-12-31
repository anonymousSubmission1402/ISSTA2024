
def remove_repeat_chars(s):
    # create a dictionary to keep track of character counts
    char_counts = {}

    # iterate over the characters in the string
    for char in s:
        # if the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1

        # otherwise, add the character to the dictionary and set its count to 1
        else:
            char_counts[char] = 1

    # create a new string with the updated characters
    new_str = ""
    for i in range(len(s)):
        char = s[i]
        if char not in char_counts or char_counts[char] == 1:
            new_str += char

    return new_str
