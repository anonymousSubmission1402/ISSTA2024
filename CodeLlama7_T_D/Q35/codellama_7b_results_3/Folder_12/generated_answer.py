
def remove_repeat_chars(s):
    # Initialize a new string to store the modified characters
    new_str = ""

    # Iterate over each character in the given string
    for char in s:

        # If the current character is not already present in the new string, append it
        if char not in new_str:
            new_str += char

    # Return the modified string
    return new_str
