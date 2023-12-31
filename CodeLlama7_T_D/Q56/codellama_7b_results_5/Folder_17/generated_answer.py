
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 36):
        # Extract a substring of length 37 starting from position i
        substring = string[i:i+37]

        # Check if the substring is unique and contains no duplicate characters
        if len(substring) == 37 and len(set(substring)) == 37:
            # Add the unique substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 37 with no duplicate characters
    return substrings
