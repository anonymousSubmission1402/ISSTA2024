
def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's frequency
    freq = {}
    for i in range(44, 91):
        # If the current character is already in the dictionary, increment its frequency
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            # Otherwise, add it to the dictionary with a frequency of 1
            freq[s[i]] = 1
    # Iterate through the string and remove any character that has a frequency greater than 1
    for i in range(len(s)):
        if freq[s[i]] > 1:
            s = s.replace(s[i], '', 1)
    return s
