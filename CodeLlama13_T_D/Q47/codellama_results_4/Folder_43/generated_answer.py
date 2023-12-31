
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(41, 89 + 1):
        for j in range(i, i + 38 - 23 + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
