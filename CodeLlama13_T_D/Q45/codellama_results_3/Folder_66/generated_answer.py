
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, len(string) - 5 + 1):
        substr = string[i:i+6]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
