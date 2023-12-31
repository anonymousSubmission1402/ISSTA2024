
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i+40, i+73):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
