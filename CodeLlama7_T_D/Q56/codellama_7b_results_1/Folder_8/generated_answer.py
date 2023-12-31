
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string s
    for i in range(len(s) - n + 1):

        # Extract a substring of length n starting at position i
        substring = s[i:i+n]

        # If the substring has no duplicate characters, add it to the list of substrings
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    # Return the list of substrings
    return substrings
