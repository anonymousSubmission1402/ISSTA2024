
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate through each character in the input string
    for char in s:

        # If the current character is between 78 and 81 (both exclusive) and is greater than 'S' and smaller than '[', remove all occurrences of that character within the input string while keeping the order of all characters intact
        if char > "S" and char < "[":
            filtered_string += char * 0

        # Otherwise, append the current character to the filtered string
        else:
            filtered_string += char

    # Return the altered input string with the filtered characters removed
    return filtered_string
