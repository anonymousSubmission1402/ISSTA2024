
def palindromes_of_specific_lengths(string):
    # Find all substrings between indices 17 and 72 (inclusive)
    substr_start = 17
    substr_end = 72
    substr_indices = range(substr_start, substr_end + 1)
    # Find all palindromes of lengths 50 to 51 in the substrings
    palindromes = []
    for substr_index in substr_indices:
        substr = string[substr_index:substr_index + 2]
        if len(substr) == 50 or len(substr) == 51:
            palindrome = ''

            # Check if the palindrome is a rotation of the original substring
            for i in range(len(substr)):
                if substr[i] != substr[-i - 1]:
                    continue

                else:
                    palindrome += substr[i]

            if len(palindrome) > 0:
                palindromes.append(palindrome)

    return set(palindromes)
