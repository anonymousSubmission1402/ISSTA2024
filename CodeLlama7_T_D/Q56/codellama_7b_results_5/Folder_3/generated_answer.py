
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 92)):
        # Extract the substring of length 93 starting from index i
        substring = input_string[i:i+93]

        # Check if the substring is already in the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 93
    return substrings
