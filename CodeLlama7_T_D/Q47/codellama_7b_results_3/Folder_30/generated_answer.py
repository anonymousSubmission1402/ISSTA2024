
def palindromes_of_specific_lengths(string):
    # create a substring of the specified range
    substring = string[14:90]
    # initialize an empty set to store the palindromes
    palindromes = set()
    # iterate over each character in the substring
    for i in range(len(substring)):
        # check if the current character is a palindrome of length 55 to 71 (both inclusive)
        if len(substring[i:]) >= 55 and len(substring[i:]) <= 71 and substring[i:] == substring[i:][::-1]:
            # add the palindrome to the set
            palindromes.add(substring[i:])
    # return the set of palindromes
    return palindromes
