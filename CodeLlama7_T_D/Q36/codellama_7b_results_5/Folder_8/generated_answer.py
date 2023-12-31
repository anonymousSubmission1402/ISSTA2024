
def filter_chars(s):
    # create a new string with the filtered characters
    new_string = ""

    # iterate over the characters in the given string
    for char in s:

        # if the current character is between the indices 82 and 93 (exclusive) and it is greater than character '!' and smaller than character '*', then remove all occurrences of that character within the string while keeping the order of all characters intact
        if char in range(82, 93) and char > "!" and char < "*":
            new_string += char

        # otherwise, just add the current character to the new string
        else:
            new_string += char

    # return the altered string
    return new_string
