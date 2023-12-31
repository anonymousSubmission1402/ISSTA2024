 def palindromes_of_specific_lengths(string):
    # create a list of all substrings in the specified range
    substrings = [string[i:i+6] for i in range(len(string)-5)]
    # filter the substrings to only include palindromes of lengths between 3 and 5
    palindromes = []
    for substring in substrings:
        if len(substring) < 3 or len(substring) > 5:
            continue

        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
