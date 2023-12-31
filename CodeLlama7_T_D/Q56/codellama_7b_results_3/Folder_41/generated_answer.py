
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the string minus the size of the substring we want to find
    for i in range(len(string) - n + 1):
        # Extract the substring of size n starting at position i in the original string
        substring = string[i:i+n]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list
            substrings.append(substring)

    # Return the list of distinct substrings of size n
    return substrings
