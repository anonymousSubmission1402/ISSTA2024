
def remove_repeat_chars(s):
    # create a dictionary to store the frequency of each character
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    # iterate through the characters in the string
    for i, c in enumerate(s):
        # if the character occurs more than once between indices 10 and 100
        if freq[c] > 1 and i >= 10 and i < 100:
            # remove all occurrences of that character from the string
            s = s.replace(c, '', freq[c])
    return s
