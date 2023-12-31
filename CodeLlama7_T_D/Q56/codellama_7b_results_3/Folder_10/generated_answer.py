
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 55 + 1)):
        # Extract a substring of length 55 starting from the current index
        substring = input_string[i:i+55]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # If it does not have any duplicates, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 55 with no duplicate characters
    return substrings
