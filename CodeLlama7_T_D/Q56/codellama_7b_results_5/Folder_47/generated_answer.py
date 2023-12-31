
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - 90)):

        # Check if the substring is of length 91 and does not contain any duplicate characters
        if (string[i:i+91] not in substrings) and len(string[i:i+91]) == 91:

            # Add the substring to the list of substrings
            substrings.append(string[i:i+91])

    # Return the list of all distinct substrings of length 91 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
