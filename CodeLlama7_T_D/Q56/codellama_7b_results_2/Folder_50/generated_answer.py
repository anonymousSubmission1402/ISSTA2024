
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 10 + 1):

        # Extract a substring of size 11 starting from the current index
        substring = string[i:i+11]

        # Check if the substring is already in the list
        if substring not in substrings:

            # Add the substring to the list
            substrings.append(substring)

    # Return the list of substrings
    return substrings
