
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 42):
        # Extract a substring of length 43 starting at index i
        substring = string[i:i+43]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list if it is unique
            substrings.append(substring)

    # Return the list of all distinct substrings of length 43 with no duplicate characters
    return substrings
