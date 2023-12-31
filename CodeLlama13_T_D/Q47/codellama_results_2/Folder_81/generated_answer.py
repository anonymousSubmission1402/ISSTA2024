
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 220 + 1):
        for j in range(12, 122 + 1):
            substr = string[j:j + i]
            if len(substr) == i and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
