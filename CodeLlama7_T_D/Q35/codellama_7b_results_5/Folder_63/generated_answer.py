 def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters
    char_count = {}

    # Iterate over the string and count the occurrences of each character
    for c in s:
        if c not in char_count:
            char_count[c] = 1

        else:
            char_count[c] += 1

    # Create a new string to store the altered characters
    new_s = ""

    # Iterate over the characters in the original string
    for c in s:

        # If the character is not present in the dictionary or it is not repeated, add it to the new string
        if c not in char_count or char_count[c] == 1:
            new_s += c

        # If the character is repeated, skip all occurrences of that character
        else:
            continue


    return new_s
