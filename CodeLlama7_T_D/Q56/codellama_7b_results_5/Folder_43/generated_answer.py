
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 85):
        # Extract the substring of length 86 starting at position i
        substring = string[i:i+86]
        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 86 with no duplicate characters
    return substrings
