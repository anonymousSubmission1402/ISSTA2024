
def filter_chars(string):
    # Create a new string with all characters removed
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the character is between indices 19 and 92, both inclusive, and is greater than or equal to character '8' and smaller than or equal to character 'm', then remove all occurrences of that character from the string
        if 19 <= len(filtered_string) + 1 <= 92 and char >= "8" and char <= "m":
            # Remove all occurrences of this character from the filtered string
            filtered_string = filtered_string.replace(char, "")

    # Return the altered string
    return filtered_string
