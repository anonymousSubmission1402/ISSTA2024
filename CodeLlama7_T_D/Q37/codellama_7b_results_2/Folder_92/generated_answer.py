
def filter_chars(s):
    # create a new string with the filtered characters
    new_str = ""
    # loop through each character in the given string
    for char in s:
        # if the current character is not between indices 4 and 4, both inclusive, and is greater than or equal to character '7' and smaller than or equal to character 'o', then add it to the new string
        if (char >= "7" and char <= "o") == False:
            new_str += char
    # return the altered string
    return new_str
