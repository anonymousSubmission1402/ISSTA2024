
def remove_repeat_chars(s):
    # Create a set of unique characters in the given string
    unique_chars = set(s)
    # Initialize an empty string to store the altered string
    altered_string = ""

    for char in s:

        # If the character is not already in the unique_chars set, add it and continue
        if char not in unique_chars:
            unique_chars.add(char)
            continue

        # If the character is already in the unique_chars set, remove all occurrences of that character from the string
        else:
            s = s.replace(char, "")

    return altered_string
