
def palindromes_of_specific_lengths(string):
    # Find the substring from index 101 to index 292, both inclusive
    substr = string[101:293]
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each letter in the substring
    for i in range(len(substr)):
        # Check if the letter is an English letter
        if substr[i].isalpha():
            # Find the length of the palindrome starting from the current index
            length = len(substr) - i
            
            # Check if the length is between 154 and 182, both inclusive
            if 154 <= length <= 182:
                # Create a string to store the palindrome
                palindrome = substr[i:length]
                
                # Reverse the string and check if it is equal to the original string
                if palindrome == palindrome[::-1]:
                    # If it is, add it to the set of palindromes
                    palindromes.add(palindrome)
    
    return palindromes
