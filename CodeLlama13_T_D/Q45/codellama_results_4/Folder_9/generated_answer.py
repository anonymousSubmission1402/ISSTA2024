
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(7, len(string)):
        substr = string[i-6:i+1]
        if all(letter in letters for letter in substr):
            rev_substr = "".join(reversed(substr))
            if substr == rev_substr:
                palindromes.add(substr)
    return palindromes
