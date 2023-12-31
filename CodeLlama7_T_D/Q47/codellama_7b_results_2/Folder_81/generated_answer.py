
def palindromes_of_specific_lengths(string):
    # Define the substring range for searching palindromes
    substr = string[12:122]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Get the substring starting from the current character and ending at the last character of the substring
        substr_i = substr[i:]
        # Check if the substring is a palindrome
        if substr_i == substr_i[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr_i)
    # Filter the palindromes based on their lengths
    filtered_palindromes = [p for p in palindromes if 12 <= len(p) <= 220]
    return filtered_palindromes
