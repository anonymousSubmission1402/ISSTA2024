 def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for i in range(len(s)):
        if s[i] not in char_freq:
            char_freq[s[i]] = 1
        else:
            char_freq[s[i]] += 1
    # Create a new string with the characters that appear only once
    new_str = ""
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            new_str += s[i]
    return new_str
