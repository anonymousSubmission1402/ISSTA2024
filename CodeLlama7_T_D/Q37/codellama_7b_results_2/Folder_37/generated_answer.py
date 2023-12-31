 def filter_chars(s):
    # create a new string with the filtered characters
    new_str = ""
    # iterate over the characters of the original string
    for i in range(len(s)):
        # if the current character is between indices 17 and 63, inclusive
        if 17 <= i <= 63:
            # and it is greater than or equal to 'O' and smaller than or equal to '^'
            if ord('O') <= ord(s[i]) <= ord('^'):
                # then we skip this character when building the new string
                continue

        # otherwise, we add the current character to the new string
        new_str += s[i]
    # return the filtered string
    return new_str
