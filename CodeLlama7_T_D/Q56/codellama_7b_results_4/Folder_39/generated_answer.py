
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 93):
        # Extract a substring of length 94 from the current position
        substring = string[i:i+94]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # If the substring is valid, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 94 with no duplicate characters
    return substrings
