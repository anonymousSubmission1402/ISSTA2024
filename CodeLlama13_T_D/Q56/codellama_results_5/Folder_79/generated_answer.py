
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the substring of length n exists in the current position
        if len(s[i:i+n]) == n:
            # Add the substring to the list of substrings
            substrings.append(s[i:i+n])
    
    # Return the list of distinct substrings
    return substrings
