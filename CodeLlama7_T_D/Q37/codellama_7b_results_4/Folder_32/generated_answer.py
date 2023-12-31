
def filter_chars(s):
    # Create an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the input string
    for char in s:
        # Check if the current character is between indices 23 and 89, inclusive
        if (char >= 'w' and char <= '{') and char != '_':
            # If it is, add it to the filtered list
            filtered.append(char)

    # Join all the filtered characters together into a single string
    filtered = ''.join(filtered)

    # Return the altered string
    return filtered
