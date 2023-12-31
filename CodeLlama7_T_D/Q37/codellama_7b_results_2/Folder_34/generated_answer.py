 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the input string
    for char in s:
        # Check if the current character is between indices 54 and 62, both inclusive
        if 54 <= ord(char) <= 62:
            # If the character is between these indices, check if it is greater than or equal to ')' and smaller than or equal to '9'
            if char >= ')' and char <= '9':
                # If the character passes this test, then it should be removed from the filtered characters list
                continue

        # If the current character does not pass the tests above, then it should be added to the filtered characters list
        filtered_chars.append(char)
    # Join the filtered characters together and return the resulting string
    return "".join(filtered_chars)
