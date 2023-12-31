 def remove_repeat_chars(s):
    # Create a new string with the same length as the original string
    new_str = ""
    # Iterate through each character in the original string
    for i in range(len(s)):
        # Check if the current character is repeated between indices 6 and 9, both exclusive
        if s.count(s[i]) > 1 and i >= 6 and i < 9:
            # Remove all occurrences of the repeated character from the original string
            s = s[:i] + s[i+1:]
    # Return the altered string
    return s
