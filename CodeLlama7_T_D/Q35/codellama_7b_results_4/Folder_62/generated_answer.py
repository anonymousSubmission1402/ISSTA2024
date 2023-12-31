
def remove_repeat_chars(s):
    # create a new string to store the result
    result = ""

    # iterate over each character in the input string
    for i in range(len(s)):

        # if the current character is not already in the result string
        if s[i] not in result:

            # add the current character to the result string
            result += s[i]

        # otherwise (if the current character is already in the result string)
        else:

            # remove all occurrences of the current character from the input string
            s = s.replace(s[i], "", 1)

    # return the altered string
    return result
