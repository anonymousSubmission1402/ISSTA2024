
def palindromes_between_indices(string):
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # convert the current character to lowercase
            char = string[i].lower()
            # loop through each character in the remaining substring of the original string
            for j in range(i + 1, len(string)):
                # check if the current character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # convert the current character to lowercase
                    other_char = string[j].lower()
                    # form the palindrome by concatenating the two characters in opposite order
                    palindrome = char + other_char
                    # check if the formed palindrome has at least 3 letters and is a valid palindrome
                    if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                        # add the formed palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # return the set of palindromes
    return palindromes
